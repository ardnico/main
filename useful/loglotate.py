#!/usr/bin/env python3

import os
import sys
import pyotp
import win32com.client
import shutil
from glob import glob
from datetime import datetime as dt
import socket
from sys import argv

class loglotation:
    def __init__(self,logname:str='logfile',outputdir:list=[os.getcwd()]):
        self.logname=logname
        self.outputdir=outputdir
        hostname = socket.gethostname()
        
        text = '[INFO]{0} started by {1}'.format(hostname)
        tdatetime = dt.now()
        today_date = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
        text = '{0} {1}\n'.format(today_date,text)
        for i in outputdir:
            with open('{0}\\{1}.log'.format(i),encoding='shift_jis',mode='a') as f:
                f.write(text)
        print(text)



    # loglotation
    def loglotate(self,lname:str='',opd:list=[],lsize:int=100000,num:int=20):
        tdatetime = dt.now()
        todate = tdatetime.strftime('%Y%m%d%H%M%S')
        today_date = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
        if lname == '':
            logname = self.logname
        else:
            logname = lname
        if len(opd) == 0:
            outputdir = self.outputdir
        else:
            outputdir = opd
        for i in outputdir:
            try:
                logsize = os.path.getsize("{0}\\{1}.log".format(i,logname))
            except:
                logsize = 0
            try:
                os.mkdir('{}\\old_log'.format(i))
            except:
                pass
            if logsize > lsize : #  lotate more than lsize log file 
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

    # Write into logfile
    def write(self,text:str='',logdir:list=[]):
        if len(logdir) == 0:
            logdir = self.outputdir
        tdatetime = dt.now()
        today_date = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
        text = '{0} {1}\n'.format(today_date,text)
        for i in logdir:
            with open('{0}\\{1}.log'.format(i),encoding='shift_jis',mode='a') as f:
                f.write(text)
        print(text)