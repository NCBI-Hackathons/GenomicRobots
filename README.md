# GenomicRobots
## Introduction:

Many datasets are not currently being available for public access and exists only in various institutional databases due to the cumbersome analytic processes involved in analysing NGS datasets and concerns over breaching a patients' genetic privacy. This may hamper current efforts towards underpinning the genetic contributors of health and diseases. We report the development of SNPBOT, a lightweight platform that simplifies the process of secure retrieval of genotypic information and offers efficient sharing between collaborators.

## Goals:

To build a a web-based tool that simplifies the process of secure retrieval of patients genotypic information adn sharing between collaborators.

## Use cases

1. Alice has unpublished, private data consisting of FASTQ files or VCF variant
   calls. Bob has a list of variants he is interested in studying. Bob would
   like to know if he could collaborate with Alice, but cannot directly access
   her data. As a pre-collaboration step, Alice runs this code on a server
   connected to her data. Bob then queries the data through a web interface,
   and the server responds with a yes or no that the variants are in the data
   set.

   This is much like the [beacon model](https://beacon-network.org), but here
   we implement an additional "strategic flipping" filtering step described
   (but not implemented) in https://www.ncbi.nlm.nih.gov/pubmed/28786360 to
   mitigate possible privacy issue by introducing a calculated amount of noise
   to the "yes" or "no" answer.

2. Charlie has unpublished FASTQ files and would prefer not to run variant
   calling. He only wants to know if his variants of interest are found in his
   FASTQ files. He runs this code on a server connected to his data, and
   queries for the variants. In this case, no noise is added to the output,
   since there are no privacy issues with Charlie using his own data.


## Target Audience:

Any institution in the BoT network can implement to share genetic data. The BoT questions of the form "Do you have information about the following mutation?" and responds with one of "Yes" or "No", among potentially more but no personal information.

## Significance:

Need to share data

Need to protect privacy

Need for a simplistic workflow for retrieving genotypic information.

## Question:

Can we simplify the process of retrival of a patients genotypic information?

## Method:

There are two operating modes:

- preprocessed VCF input
- raw FASTQ file

The strategic flipping method requires alternative allele frequencies to be
computed on the local data, and therefore data needs to be preprocessed into
VCFs with allele frequencies.. In cases where this is infeasible, raw FASTQs
can be used, and [PSST](https://github.com/NCBI-Hackathons/PSST) is used to
identify variants in the FASTQ files.

This latter mode is additionl

A web app accepts a list of variants.

Depending on the configuration, these variants are either checked directly
against a pool of configured VCF files, or checked against configured FASTQ
files. When querying against VCFs, we can use the strategic flipping method to
add noise to the output to mitigate security and privacy concerns.



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


## To run Web application:

Set up python environment (conda or virtualenv or both) using requirements.txt. 
Edit config files connecting web application with Snakemake pipeline

```
python -m genomicrobots runserver -h 0.0.0.0
```
Open your web browser at port 5000.


## Anticipated results:

A simplistic web-based tool that simplifies extraction of genotypic information.

# Conclusion:

Our findings suggests most institutions have databases through which de-identified genomic data can be shared but the issue of a simplistic workflow to retrieve and share genotypic information remains a major challenge. This web-based tool simplifies the process of retrieving genotypic information for sharing among institutions within the network.
# People

Alexander Goncearenco: alexandr.goncearenco@nih.gov
Bari Ballew: bari.ballew@nih.gov
Daler: dalerr@niddk.nih.gov
Justin Ideozu: jideozu@luriechildrens.org
kishore Anekalla: kishore.anekalla@northwestern.edu
Sophia Liu: ssliu@u.northwestern.edu

