#!/usr/bin/env python3

import chardet
import pandas as pd

class read_data(object):
    def __init__(self,fpath):
        self.fpath = fpath

    def df(self,fpath='', **kwargs):
        if fpath == '':
            fpath = self.fpath
        with open(fpath, mode='rb') as f:
            encflag = f.read()
        encode = chardet.detect(encflag)['encoding']
        print('encode: {0}'.format(encode))
        if fpath[-3:].lower() == 'csv':
            try:
                df = pd.read_csv(fpath,encoding='utf-8',*kwargs)
            except:
                df = pd.read_csv(fpath,encoding=encode,*kwargs)
        else:
            df = pd.read_excel(fpath,encoding=encode,*kwargs)
        return df