#!/usr/bin/env python

import requests, sys, json


def maf_by_rsid(ids):
    """
    Returns a dict of minor allele frequencies for each provided rsID.


    Queries the Ensembl REST API; currently unknown what the limitation are in
    terms of requests or size of ID list.

    Parameters
    ----------
    ids : list
        List of SNP IDs. We're using the Ensembl REST API, so ids can be any
        supported Ensembl ID (even a mixture in the same list)
    """

    # TODO: multiprocess.Pool to run multiple requests of reasonable batch-size
    # simultaneously

    server = "https://rest.ensembl.org"
    ext = "/variation/homo_sapiens"
    headers= {
        "Content-Type" : "application/json",
        "Accept" : "application/json"
    }

    ids = [i.strip() for i in open('rsids.txt')][:4]
    r = requests.post(server+ext, headers=headers, data=json.dumps({'ids': ids}))
    if not r.ok:
      r.raise_for_status()
      sys.exit()
    decoded = r.json()
    return {k: v['MAF'] for k, v in decoded.items()}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(usage='Filter provided rsIDs by MAF.')
    ap.add_argument('--ids', help=''''Filename containing variant IDs. If not
                    provided, uses stdin. Commented-out lines are ignored''')
    ap.add_argument('--thresh', default=0.01, type=float, help='''Threshold at which rsIDs
                    with MAF below this value will not be reported in the
                    output''')
    args = ap.parse_args()
    ids = []
    if args.ids:
        fin = open(args.ids)
    else:
        fin = sys.stdin

    for i in f:
        if i.startswith('#'):
            continue
        i = i.strip()
        if i:
            ids.append(i)
    res = maf_by_rsid(ids)
    valid = []
    for i in ids:
        try:
            if res[i] < args.thresh:
                continue
        except KeyError:
            continue
        print(i)

