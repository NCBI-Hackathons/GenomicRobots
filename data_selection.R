#!/usr/bin/env Rscript
#install.packages("tidyverse")
library(tidyverse)
arguments <- commandArgs(TRUE)

# Read SRA file
# get sra file metainfo from PRJNA262923
SraRunInfo <- read.csv("SraRunInfo.csv")
# taking only whole genome seq data 
wgs<-SraRunInfo %>% 
  filter(LibraryStrategy == "WGS")
# select only required columns of interest
# we can get the download path by appending https://sra-download.ncbi.nlm.nih.gov/srapub/
# before srr id 
finaldat<-wgs %>% 
  select(Run,Experiment,SRAStudy,BioProject,ProjectID,
         Sample,BioSample,SampleName,Sex)
write.csv(finaldat,"1000_genomes_req_samples.csv",row.names = FALSE)
