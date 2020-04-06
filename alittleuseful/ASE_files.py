#!/usr/bin/env python3

import getpass
import os
import Crypto.Cipher.AES as AES
from glob import glob
key = b'0123456789abcdef'
iv = b'0' * 16
basecode = '****************'
filepath = '{0}\\data\\enc'.format(os.getcwd())
try:
    os.makedirs(filepath)
except:
    pass

class ASE_files(object):
    def __init__(self):
        super().__init__()

    def encryption(self,filename,passcode):
        if len(glob('{0}\\{1}*'.format(filepath,filename))) > 0:
            print('This filename already used')
            raise Exception
        passcode = str(passcode)
        pass_length = len(passcode)
        encarry = []
        i = 0
        while True:
            enctarget = passcode[(16*(i)):(16*(i+1))]
            if len(enctarget) == 0:
                break
            elif len(enctarget) < 16:
                for j in range(16-len(enctarget)):
                    enctarget += '*'
            encarry.append(enctarget)
            i += 1
        aes = AES.new(key, AES.MODE_CBC, iv)
        for ij in range(len(encarry)):
            cipher = aes.encrypt(encarry[ij].encode('ascii'))
            number = format(ij, '0>3')
            with open('{0}\\{1}{2}.aes'.format(filepath,filename,number), mode="wb") as fout:
                bary = bytearray(cipher)
                bary.append(0)
                bary.extend([1, 127])
                fout.write(bary)
        print('Completed Encryption')
        return 


    def decription(self,filename):
        files = glob('{0}\\{1}[0-9][0-9][0-9].aes'.format(filepath,filename))
        if len(files) == 0:
            print('Such file is not found:{}'.format(filename))
            raise Exception
        decode_line = ''
        aes = AES.new(key, AES.MODE_CBC, iv)
        for file in files:
            bdata = open(file, "rb").read()
            bdata2 = bytearray(bdata)
            for three in range(3):
                bdata2.pop()
            decode_text = aes.decrypt(bdata2).decode('ascii')
            decode_text = decode_text.replace('*','')
            decode_line += decode_text
        return decode_line


    def dell_enc_data(self,filename):
        files = glob('{0}\\{1}[0-9][0-9][0-9].aes'.format(filepath,filename))
        if len(files) == 0:
            print('Such file is not found:{}'.format(filename))
            raise Exception
        for file in files:
            os.remove(file)
        print('completed to delete')


