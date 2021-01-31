import os
import sys
import shutil
from glob import glob
from datetime import datetime as dt

# dt.now().strftime('%Y/%m/%d %H:%M:%S')
default_log_locale = fr"{os.getcwd()}\log"

class log_writer():
    def __init__(self,log_locale:str="",gen="",vol="",name=""):
        self.log_locale = log_locale
        self.gen = gen
        self.vol = vol
        self.name = name
    
    def lotate_logfile(self,gen="",vol="",name=""):
        if gen!="":
            self.gen = gen
        if vol!="":
            self.vol=vol
        if name!="":
            self.name=name
        self.vol = int(self.vol)
        self.gen = int(self.gen)
        filename = fr"{self.log_locale}\{self.name}.log"
        toname = fr"{self.log_locale}\{self.name}_{dt.now().strftime('%Y%m%d%H%M%S')}.log"
        try:
            log_size = os.path.getsize(filename)
        except:
            log_size = 0
        if log_size > self.vol:
            files = glob(fr"{self.log_locale}\{self.name}_??????????????.log")
            if len(files) > self.gen:
                target = files[0]
                while len(files) > self.gen:
                    tmpdata = 99999999999
                    for file in files:
                        if tmpdata > int(os.stat(file).st_mtime):
                            tmpdata = int(os.stat(file).st_mtime)
                            target = file
                    os.remove(target)
                    infmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[SUCCESS]This logfile lotated : {target}"
                    print(infmsg)
                    files = glob(fr"{self.log_locale}\{self.name}_??????????????.log")
            os.rename(filename, toname)
    
    def set_log_place(self,log_locale:str="",gen:int="",vol:int="",name=""):
        if gen!="":
            self.gen = gen
        elif self.gen=="":
            self.gen = 5
        if vol!="":
            self.vol = vol
        elif self.vol=="":
            self.vol = 100000
        if name!="":
            self.name = name
        elif self.name=="":
            self.name = "logfile"
        if self.log_locale=="":
            self.log_locale = default_log_locale
        if log_locale!="":
            if log_locale[-1] == "\\":
                log_localse = log_locale[:-1]
            self.log_locale = log_locale
        try:
            os.mkdir(self.log_locale)
        except:
            pass
    
    def write_log(self,level,message):
        error_explain = """"level list
    1:  INFO
    2:  WARN
    3:  ERROR
    4:  FATAL
    5:  EMERGE
"""
        if level==1:
            lmsg = "INFO"
        elif level==2:
            lmsg = "WARN"
        elif level==3:
            lmsg = "ERROR"
        elif level==4:
            lmsg = "FATAL"
        elif level==5:
            lmsg = "EMERGE"
        else:
            print(error_explain)
            raise SyntaxError(error_explain)
        if self.log_locale=="":
            errmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[ERROR]Please set parameters by this command line [set_log_place(log_locale:str,gen:int,vol:int,name:str)]"
            raise SyntaxError(errmsg)
        try:
            message = str(message)
        except TypeError:
            mtype = type(message)
            errmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[ERROR]Because the message type was {mtype}, failed to convert string type."
            print(e)
            raise Exception(errmsg)
        try:
            logfilename = fr"{self.log_locale}\{self.name}.log"
            with open(logfilename,mode="a") as f:
                f.write(f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[{lmsg}]{message}")
                f.write("\n")
        except Exception as e:
            errmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[ERROR]Failed to write a message: {message}"
            print(e)
            raise Exception(errmsg)
        try:
            self.lotate_logfile(gen=self.gen,vol=self.vol,name=self.name)
        except Exception as e:
            logfilename = fr"{self.log_locale}\{self.name}.log"
            errmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}[ERROR]Failed to lotate the logfile:{logfilename}"
            print(e)
            raise Exception(errmsg)
        return 0


