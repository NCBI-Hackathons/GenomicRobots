# GenomicRobots
## Introduction:

Although issues of re-identication are a major concern for use of genomic data, most instituitions including the NIH have now developed databases through which de-identified information can be shared. However, current efforts towards retrieval/sharing of genotypic data are hampered due to the cumbersome analytic processes that may be involved in analysing NGS datasets.

## Goals: 

To build a a web-based tool that simplifies the process of retrieving patients genotypic information.

## Target Audience: 

Any institution in the BoT network can implement to share genetic data. The BoT questions of the form "Do you have information about the following mutation?" and responds with one of "Yes" or "No", among potentially more but no personal information. 


# Significance: 

Need to share data 

Need to protect privacy

Need for a simplistic workflow for retrieving genomic information. 

# Question: 

Can we simplify the process of retrival of a patients  genotypic information?  

# Method:

Fastq file -> implement the psst pipeline -> yes or no output 

The PSST (NCBI Hackathon; La 2017) pipeline is as follows:

    Extracts flanking sequences for the SNP accessions and creates a FASTA file containing these flanking sequences.

    Creates a BLAST database out of the SNP flanking sequences.

    Runs Magic-BLAST on each phenotype-associated SRA dataset and the SNP flanking sequence BLAST database.

    From the Magic-BLAST alignments, determines which SNPs are contained in the SRA datasets using a statistical heuristic.
    
# Anticipated results: 

A simplistic web-based tool that simplifies extraction of genotypic information.

## To run PSST:

psst.sh -s <samples_list> -n <rsids_list> -d <.> -e <email> -t <n> -p <n>

see https://github.com/NCBI-Hackathons/PSST for more details

### Input files:
- samples_list (e.g. testsamples.in) is a list of SRA accessions (one per line) 
  OR
- path/to/fastq
  - can only accept a single path and filename, not a list
- rsids_list (e.g. testsnps.in) is a list of rsIDs (one per line, with the "rs" removed)

### Output file:
- (e.g. test.out (renamed for testing; typically named results.tsv))
- three tab-delimited columns with a header row
  - first column is SRA accession number (or filename if fastq used)
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

- output files: 
  - feature_matrix.csv
  - maf_table.csv
