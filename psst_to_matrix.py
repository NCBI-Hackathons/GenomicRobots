#!/usr/bin/env python3

import argparse
import sys
import csv
import pandas as pd

###############################################
################## Functions ##################
###############################################


def check_file(fname):
    """Check that file can be read, exit with error message if it can not."""

    try:
        f = open(fname, 'rb')
    except IOError:
        print("Could not read file ", fname)
        sys.exit()

    f.close()

###############################################


def get_dict(myKey, myValue, dosage, featureList, myDict):
    """Convert PSST report to gene dosage dict."""

    myList = myValue.split(',')
    myList.insert(0, myKey)
    tempList = []
    for x in featureList:
        if x in myList:
            tempList.append(dosage)
        else:
            tempList.append(0)
    myDict[myKey] = tempList
    return myDict

###############################################
################ End functions ################
###############################################


# handle command line arguments
parser = argparse.ArgumentParser(description = 'Takes PSST output and converts to gene dosage sample x snp matrix.')
parser.add_argument('psst_snps_in', help='List of SNPs run through PSST')
parser.add_argument('psst_samples_in', help='List of samples with path to fastq run through PSST')
results = parser.parse_args()

# for debugging
# print('psst_snps_in    = ', results.psst_snps_in)
# print('psst_samples_in = ', results.psst_samples_in)

# check for presence of files
check_file(results.psst_snps_in)
check_file(results.psst_samples_in)

# read in all queried snps
with open(results.psst_snps_in) as f:
    snps = f.readlines()
    snps = [x.strip('\n') for x in snps] 
    snps = [x for x in snps if x]

het_dict = {}
hom_dict = {}
sample_count = 0
# read in all queried samples
with open(results.psst_samples_in) as f:
    for line in csv.reader(f, delimiter="\t"):  # works for sra accession numbers; what about fastq?
        if (len(line) == 0) or (line[0].startswith('#')):
            continue
        psst_out = line[0] + "/results.tsv"
        check_file(psst_out)
        sample_count = sample_count + 1
        print(psst_out)
        # read in het/hom snps found
        with open(psst_out) as f:
            next(f)  # skip header
            for line in csv.reader(f, delimiter="\t"):
                    # convert het and hom snps to gene dosage matrix
                    get_dict(line[0], line[1], 1, snps, het_dict)
                    get_dict(line[0], line[2], 2, snps, hom_dict)

# check dicts for presence of all samples queried
# for x in samples:
#     if x not in het_dict:
#         het_dict[x] = [0] * len(snps)
#     if x not in hom_dict:
#         hom_dict[x] = [0] * len(snps)

# create dataframes and sum het/hom data
df1 = (pd.DataFrame(het_dict)).T
df2 = (pd.DataFrame(hom_dict)).T
df = df1.add(df2)
df.columns = snps
# print(df)
df.to_csv("feature_matrix.csv")

# calculate MAF within the queried population
df_maf = df.T
df_maf['sum'] = df_maf.sum(axis=1)
df_maf['maf'] = df_maf['sum'] / (sample_count * 2)
df_maf = df_maf.filter(['maf'])
# print(df_maf)
df_maf.to_csv("maf_table.csv")
