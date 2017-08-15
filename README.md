# GenomicRobots

## To run PSST:

psst.sh -s <samples_list> -n <rsids_list> -d <.> -e <email> -t <n> -p <n>

see https://github.com/NCBI-Hackathons/PSST for more details

### Input files:
- samples_list (e.g. testsamples.in) is a list of SRA accessions (one per line) or fastq???  (still testing)
- rsids_list (e.g. testsnps.in) is a list of rsIDs (one per line, with the "rs" removed)

### Output file:
- (e.g. test.out (renamed for testing; typically named results.tsv))
- three tab-delimited columns with a header row
  - first column is SRA accession number
  - second column is list of rsIDs (no "rs") detected as hets
  - third column is list of rsIDs (no "rs") detected as hom alt

### Notes:
- Make sure magicblast is installed and added to path

## To run psst_to_matrix.py:

```
usage: psst_to_matrix.py [-h] psst_snps_in psst_samples_in psst_out

Takes PSST output and converts to gene dosage sample x snp matrix.

positional arguments:
  psst_snps_in     List of SNPs run through PSST
  psst_samples_in  List of samples run through PSST
  psst_out         PSST output file

optional arguments:
  -h, --help       show this help message and exit
  ```

- example output: feature_matrix.csv
