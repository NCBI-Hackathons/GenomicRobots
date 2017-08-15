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
    
## Anticipated results: 

A simplistic web-based tool that simplifies extraction of genotypic information.

## Conclusion: 
Our findings showed most institutions have databases through which de-identified genomic data can be shared but the issue of a simplistic workflow to retrieve and share genotypic information remains a major challenge. This web-based tool simplifies the process of retrieving genotypic information for sharing among institutions within the network.
