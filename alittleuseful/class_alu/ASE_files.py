#!/usr/bin/env python3

import getpass
import os
from cryptography.fernet import Fernet
from glob import glob
default_key =b'FtnAwI-FffemOcnifdEnraenu_dOGFxFfkcoTSftiER='
default_dir = fr'{os.getcwd()}\data\enc'
class ASE_files(object):
    def __init__(
        self,
        encfile=default_dir,
        key=default_key
        ):
        self.encfile = encfile

    def encryption(self,filename,passcode):
        try:
            os.makedirs(self.encfile)
        except:
            pass
        if len(glob(fr'{filepath}\{filename}*')) > 0:
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
        f = Fernet(key)
        for ij in range(len(encarry)):
            cipher = f.encrypt(encarry[ij].encode('ascii'))
            number = format(ij, '0>3')
            with open(f'{filepath}\\{filename}{number}.aes', mode="wb") as fout:
                bary = bytearray(cipher)
                fout.write(bary)
        print('Completed Encryption')
        return 


    def decription(self,filename):
        files = glob(f'{filepath}\\{filename}[0-9][0-9][0-9].aes')
        if len(files) == 0:
            print(f'Such file is not found:{filename}')
            raise Exception
        decode_line = ''
        f = Fernet(key)
        for file in files:
            bdata = open(file, "rb").read()
            decode_text = f.decrypt(bdata).decode('ascii')
            decode_text = decode_text.replace('*','')
            decode_line += decode_text
        return decode_line


    def dell_enc_data(self,filename):
        files = glob(f'{filepath}\\{filename}[0-9][0-9][0-9].aes')
        if len(files) == 0:
            print(f'Such file is not found:{filename}')
            raise Exception
        for file in files:
            os.remove(file)
        print('completed to delete')


