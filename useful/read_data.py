#!/usr/bin/env python3

import chardet
import pandas as pd

def read_data(fpath):
    with open(fpath, mode='rb') as f:
        encflag = f.read()
    encode = chardet.detect(encflag)['encoding']
    print('encode: {0}'.format(encode))
    if fpath[-3:] == 'csv':
        try:
            df = pd.read_csv(fpath,encoding='utf-8',dtype='str')
        except:
            df = pd.read_csv(fpath,encoding=encode,dtype='str')
    else:
        df = pd.read_excel(fpath,encoding=encode,dtype='str')
    return df
