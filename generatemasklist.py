import numpy as np
import pandas as pd
import glob as glob
import argparse
import os.path

def compileallAF(filepath, tail, ftype):
    # creates clean dataframs of local and global AFs
    filelist = glob.glob(filepath+tail)
    chromfilslist = []
    for file in filelist:
        if ftype == 'global':
            temp = pd.read_csv(file, sep='\t', header=None)
            temp.columns = ['ID', 'AF']
            temp = temp[temp.AF.str.contains(",") == False]
            temp = temp[temp.ID.str.contains(";") == False]
            temp = temp[temp.ID.str.contains("esv") == False]
            temp.to_csv('./temp.csv', sep='\t', index=False)
            temp = pd.read_csv('./temp.csv', sep='\t', dtype={'AF':np.longdouble}, index_col='ID')
            chromfilslist.append(temp)
        else:
            temp = pd.read_csv(file, sep='\t')
            temp = temp[temp.ID.str.contains(";") == False]
            temp = temp[temp.ID.str.contains("esv") == False]
            temp.to_csv('./temp.csv', sep='\t', index=False)
            temp = pd.read_csv('./temp.csv', sep='\t', dtype={'AF':np.longdouble}, index_col='ID')
            chromfilslist.append(temp)

    AF = pd.concat(chromfilslist)
    return AF

def calculate_deltD(globaldf, localdf):
    #creates list of snps to mask
    nsamples = 186
    loggamma = -6
    gamma = 0.000001
    mergeddf = localdf.join(globaldf, how='outer').fillna(0)
    mergeddf.loc[mergeddf['CALC_AF'] > 0, 'x'] = 1
    mergeddf.loc[mergeddf['CALC_AF'] <= 0, 'x'] = 0
    mergeddf['invx'] = 1-mergeddf['x']
    mergeddf['dn1'] = np.power((1-mergeddf['AF']),2*(nsamples-1))
    mergeddf['dn'] = np.power((1-mergeddf['AF']),2*(nsamples))
    mergeddf['a'] = (2*mergeddf['x']-1)*(np.log10(1-gamma*mergeddf['dn1'])-np.log10(1-mergeddf['dn']))  
    mergeddf['b'] = (1-2*mergeddf['x'])*(2*np.log10(1-mergeddf['AF'])-6)    
    mergeddf['deltD'] = mergeddf['a'] - mergeddf['b']
    l = len(mergeddf)
    a = mergeddf.sort(columns=['deltD'])[['deltD']]
    indlist = a.iloc[:int(l*0.05)].index
    return(indlist)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-g', help='globalAFfolder')
    parser.add_argument('-l', help='localAFfolder')
    args = parser.parse_args()
    localAF = compileallAF(args.l, '*.rs', 'global')
    globalAF = compileallAF(args.g, '*.txt', 'local')[['CALC_AF']]
    print(calculate_deltD(globalAF, localAF))
