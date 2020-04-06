#!/usr/bin/env python3

import chardet
import pandas as pd

class read_data(object):
    def __init__(self):
        super().__init__()

    def read_data(self,fpath,skiprows=0,dtype='str',sep=','):
        with open(fpath, mode='rb') as f:
            encflag = f.read()
        encode = chardet.detect(encflag)['encoding']
        print('encode: {0}'.format(encode))
        if fpath[-3:].lower() == 'csv':
            try:
                df = pd.read_csv(fpath,encoding='utf-8',dtype=dtype,skiprows=skiprows,sep=sep)
            except:
                df = pd.read_csv(fpath,encoding=encode,dtype=dtype,skiprows=skiprows,sep=sep)
        else:
            df = pd.read_excel(fpath,encoding=encode,dtype=dtype,skiprows=skiprows,sep=sep)
        return df