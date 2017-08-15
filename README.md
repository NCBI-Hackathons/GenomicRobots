# GenomicRobots
## Introduction:

NGS datasets no longer only exist in a few centralized locations. Sharing genotypic data is hampered due to both the cumbersome analytic processes involved in analysing NGS datasets and lack of accessibility. This is a lightweight platform that allows reasearchers to conduct prelimianry analysis on despersive sets of NGS data.

## Goals: 

To build a a web-based tool that simplifies the process of retrieving patients genotypic information.

## Target Audience: 

Any institution in the BoT network can implement to share genetic data. The BoT questions of the form "Do you have information about the following mutation?" and responds with one of "Yes" or "No", among potentially more but no personal information. 

## Significance: 

Need to share data 

Need to protect privacy

Need for a simplistic workflow for retrieving genomic information. 

## Question: 

Can we simplify the process of retrival of a patients  genotypic information?  

## Method:

Fastq file -> implement the psst pipeline -> yes or no output 

The PSST (NCBI Hackathon; La 2017) pipeline is as follows:

1. Extracts flanking sequences for the SNP accessions and creates a FASTA file containing these flanking sequences.

2. Creates a BLAST database out of the SNP flanking sequences.

3. Runs Magic-BLAST on each phenotype-associated SRA dataset and the SNP flanking sequence BLAST database.

4. From the Magic-BLAST alignments, determines which SNPs are contained in the SRA datasets using a statistical heuristic.


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

## Anticipated results: 

A simplistic web-based tool that simplifies extraction of genotypic information.

# Conclusion: 

Our findings showed most institutions have databases through which de-identified genomic data can be shared but the issue of a simplistic workflow to retrieve and share genotypic information remains a major challenge. This web-based tool simplifies the process of retrieving genotypic information for sharing among institutions within the network.
