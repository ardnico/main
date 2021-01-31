#!/usr/bin/env python3
import os
import psutil
from glob import glob
from py_surveillance.class_file_ps.wlog import *

default_set_locale = fr"{os.getcwd()}\lotate_setting.txt"
default_set_data = """[]

"""

class lotate_files():
    def __init__(self,log_locale=""):
        self.log_locale = log_locale
    
    def set_para(self,set_locale=default_set_locale):
        try:
            os.mkdir(self.log_locale)
        except:
            pass
        # if os.path.exists(set_locale)==False:
            # try:
            #     with open(set_locale,mode="w") as f:
            #         f.write(set_data)
            #     logmsg = f"{dt.now().strftime('%Y/%m/%d %H:%M:%S')}"
            # except:
                
            # # with open()


# # core count
# psutil.cpu_count()
# # logical core
# psutil.cpu_count(logical=False)




