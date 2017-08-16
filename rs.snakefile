vcf_pattern = '/home/ubuntu/data/1000_genomes_reads/vcf_files_20130502/ALL.{chrom}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz'
out_pattern = '/home/ubuntu/data/1000_genomes_reads/vcf_files_20130502/ALL.{chrom}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.rs.tab'

chroms = ['chr' + i for i in list(range(1, 23)) + ['X', 'Y']]
targets = expand(out_pattern, chrom=chroms))

rule snpsift:
    input: vcf_pattern
    output: out_pattern
    shell:
        'SnpSift {input} ID AF AC AN EAS_AF EUR_AF AFR_AF SAS_AF > {output}'


# vim: ft=python
