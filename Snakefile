import os
import pandas as pd
import yaml

config.update(yaml.load(open('config.yaml')))
SAMPLES_FILE = config['samples_table']

if 'SESSION_ID' not in os.environ:
    SNPS_FILE = 'testsnps.in'
    TMPDIR = 'output'
else:
    SNPS_FILE = config['tmp_pattern'].format(SESSION_ID=os.environ['SESSION_ID'])
    TMPDIR = os.path.dirname(SNPS_FILE)

SAMPLES = pd.read_table(
        SAMPLES_FILE,
        comment="#",
        index_col=0,
        names=['sampleid', 'path']
)['path'].to_dict()

sample_ids = list(SAMPLES.keys())
fastqs = list(SAMPLES.values())

# TODO: what thresh makes sense?
MIN_MAF = 0.01


targets = [
    fastqs,
    expand('{tmpdir}/feature_matrix.csv', tmpdir=TMPDIR),
    os.path.join(TMPDIR, 'output.txt')
]


rule all:
    input: targets


rule pre_filter_ids:
    input:
        rsids=SNPS_FILE
    output: os.path.join(TMPDIR, 'filtered_rsids.txt')
    shell:
        'python filter_ids.py '
        '--ids {input} '
        '--thresh {MIN_MAF} '
        '> {output}'


# PSST uses IDs without the "rs", so we strip those here.
rule strip_rs:
    input: os.path.join(TMPDIR, 'filtered_rsids.txt')
    output: os.path.join(TMPDIR, 'stripped_rs.list')
    shell:
        'sed "s/^rs//g" {input} > {output}'


rule psst:
    input:
        rsids=os.path.join(TMPDIR, 'stripped_rs.list'),
        fastq=lambda wildcards: SAMPLES[wildcards.sampleid]
    output:
        '{sampleid}/results.tsv'
    threads: 8
    conda:  'py2env.yaml'
    shell:
        'mkdir -p {wildcards.sampleid} && cd {wildcards.sampleid} &&'
        'PATH=/home/ubuntu/daler/PSST:/home/ubuntu/bballew/ncbi-magicblast-1.2.0/bin/:$PATH '
        'psst.sh -f {input.fastq} -n ../{input.rsids} -d . -e none@example.com -t {threads} -p {threads}'


rule post_psst:
    input:
        samples_file=SAMPLES_FILE,
        rsids=os.path.join(TMPDIR, 'stripped_rs.list'),
        psst=expand('{sampleid}/results.tsv', sampleid=sample_ids)
    output:
        out_matrix='{tmpdir}/feature_matrix.csv',
        maf_table='{tmpdir}/maf_table.csv',
    shell:
        'python psst_to_matrix.py '
        '{input.rsids} '
        '{input.samples_file} '
        '--out_matrix {output.out_matrix} '
        '--maf_table {output.maf_table} '

rule post_filter:
    input:
        out_matrix=rules.post_psst.output.out_matrix,
        rsids=os.path.join(TMPDIR, 'stripped_rs.list'),
    output: os.path.join(TMPDIR, 'output.txt')
    run:
        df = pd.read_table(input, index_col=0).transpose()
        ids = [i.strip() for i in open(input.rsids)]
        found = list(df.index[df.sum(axis=1) > 0])
        with open(output[0], 'w') as fout:
            for i in found:
                fout.write(i + '\n')


# vim: ft=python
