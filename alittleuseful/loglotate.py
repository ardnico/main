#!/usr/bin/env python3

import os
import sys
import shutil
from glob import glob
from datetime import datetime as dt
import socket
from sys import argv

pyfilename = argv[0].replace(os.getcwd(),'').replace('.py','').replace('\\','')

class loglotate(object):
    def __init__(
        self,
        logname:str=pyfilename,
        outputdir:list=[os.getcwd()],
        firsttext:str = '[INFO]{0} started by {1}'.format(pyfilename,socket.gethostname()),
        lsize:int=100000,
        num:int=20,
        timestanp:int = 1    
    ):
        self.logname=logname
        self.outputdir=outputdir
        
        tdatetime = dt.now()
        todate = tdatetime.strftime('%Y%m%d%H%M%S')
        today_date = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
        if timestanp == 1:
            text = '{0} {1}\n'.format(today_date,firsttext)
        else:
            test = firsttext

        for i in outputdir:
            try:
                logsize = os.path.getsize("{0}\\{1}.log".format(i,logname))
            except:
                logsize = 0
            try:
                os.mkdir('{}\\old_log'.format(i))
            except:
                pass
            if logsize > lsize : #  circulate log files
                shutil.move("{0}\\{1}.log".format(i,logname),'{0}\\old_log\\{1}_{2}.log'.format(i,logname,todate))
            try:
                oldlogfiles = glob('{0}\\old_log\\{1}*.log'.format(i,logname))
            except:
                print('Please check the previlage to access this directory')
                print(i)
            while len(oldlogfiles) > num:  # limit number of log files
                try:
                    os.remove(oldlogfiles[0])
                    oldlogfiles = glob('{0}\\old_log\\{1}*.log'.format(i,logname))
                except:
                    import traceback
                    traceback.print_exc()
            with open('{0}\\{1}.log'.format(i,logname),encoding='shift_jis',mode='a') as f:
                f.write(text)
        if text != "":
            print(text)

    # Write into logfile
    def write(
        self,
        text:str='',
        logdir:list=[]
    ):
        if len(logdir) == 0:
            logdir = self.outputdir
        else:
            self.outputdir = logdir
        tdatetime = dt.now()
        today_date = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
        text = '{0} {1}\n'.format(today_date,text)
        for i in logdir:
            with open('{0}\\{1}.log'.format(i,self.logname),encoding='shift_jis',mode='a') as f:
                f.write(text)