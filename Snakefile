import pandas as pd

# TODO: this will eventually be configured on the server; for now use the
# example SRRs
SAMPLES_FILE = 'testsamples.in'
SNPS_FILE = 'testsnps.in'

fastqs = [i.strip() for i in open(SAMPLES_FILE).readlines()]


# TODO: what thresh makes sense?
MIN_MAF = 0.01

targets = [
    expand('{fastq}/answer.txt', fastq=fastqs),
    'answer.txt'
]


rule all:
    input: targets


rule pre_filter_ids:
    input:
        rsids=SNPS_FILE
    output: 'filtered_rsids.txt'
    shell:
        'python filter_ids.py '
        '--ids {input} '
        '--thresh {MIN_MAF} '
        '> {output}'


# PSST uses IDs without the "rs", so we strip those here.
rule strip_rs:
    input: 'filtered_rsids.txt'
    output: 'stripped_rs.list'
    shell:
        'sed "s/^rs//g" {input} > {output}'


rule psst:
    input:
        rsids='stripped_rs.list',
    output: '{fastq}/out.csv'
    shell:
        'psst_to_matrix.py '
        '{input.rsids} '
        '{SAMPLES_FILE} '
        '{output} '


rule answer:
    input: '{fastq}/out.csv',
    output: '{fastq}/answer.txt'
    run:
        # TODO: actually write this
        shell('touch {output}')


rule aggregate:
    input: expand('{fastq}/answer.txt', fastq=fastqs)
    output: 'answer.txt'
    run:

        # TODO: this is where we have to make various decisions about what/how
        # to report
        for i in input:
            df = pd.read_table(i)
        shell('touch {output}')

# vim: ft=python
