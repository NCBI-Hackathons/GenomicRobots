#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import argparse
import pandas as pd

def check_snps(snpid,file):
    #snpid_req_file=pd.read_table("/tmp/{SESSION_ID}/rsid.txt")
    #snpid_req_file=pd.read_table("rsid.txt")
    features = pd.read_csv("/Users/kra804/Documents/test_feature/GenomicRobots/feature_matrix.csv",index_col=0).transpose()
    #features = pd.read_csv("/home/ubuntu/daler/PSST/feature_matrix.csv",index_col=0).transpose()
    rsids=list(features[features.sum(axis=1) > 0].index)
    rsids.__len__() # we have these many matches
    snpid=str(snpid)
    return (snpid in rsids)

 if __name__ == "__main__":
 	check_snps(snpid,file)
