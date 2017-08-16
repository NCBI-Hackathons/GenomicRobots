import glob

vcfs = glob.glob('/home/ubuntu/data/1000_genomes_reads/vcf_files_20130502/*.vcf.gz')
targets = [i + '.rs.tab' for i in vcfs]
print(targets)
rule all:
    input: targets

rule snpsift:
    input: '{prefix}.vcf.gz'
    output: '{prefix}.vcf.gz.rs.tab'
    shell:
        'SnpSift extractFields {input} ID AF AC AN EAS_AF EUR_AF AFR_AF SAS_AF > {output}'


# vim: ft=python
