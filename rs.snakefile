# Extracts allele frequency and other related fields from 1000 Genomes VCF
# files into a tab-delimited file keyed by rsID

import os
import glob

VCF_PATH = '/hom/ubuntu/data/1000_genomes_reads/vcf_files_20130502'
vcfs = glob.glob(os.path.join(VCF_PATH, '*.vcf.gz'))

def filt(x):
    """
    Filtering logic for VCFs here. For example, chrMT VCFs don't have all the
    subpopulation AFs
    """
    if 'chrMT' in x:
        return False
    return True

vcfs = list(filter(vcfs))

targets = [i + '.rs.tab' for i in vcfs]


rule all:
    input: targets


rule snpsift:
    input: '{prefix}.vcf.gz'
    output: '{prefix}.vcf.gz.rs.tab'
    shell:
        'SnpSift extractFields {input} ID AF AC AN EAS_AF EUR_AF AFR_AF SAS_AF > {output}'


# vim: ft=python
