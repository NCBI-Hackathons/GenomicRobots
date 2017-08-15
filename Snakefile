import pandas as pd

# TODO: this will eventually be configured on the server; for now use the
# example SRRs
SAMPLES_FILE = 'testsamples.in'
fastqs = [i.strip() for i in open(SAMPLES_FILE).readlines()]


# TODO: what thresh makes sense?
MIN_MAF = 0.01

targets = [
    expand('{fastq}_answer.txt', fastq=fastqs),
    'answer.txt'
]


rule pre_filter_ids:
    input:
        rsids='rsid_list'
    output: 'filtered_rsids.txt'
    shell:
        'filter_ids.py '
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

rule aggregate:
    input: expand('{fastq}/out.csv', fastq=fastqs)
    output: 'answer.txt'
    run:
        # TODO: this is where we have to make various decisions about what/how
        # to report
        for i in input:
            df = pd.read_table(i)

