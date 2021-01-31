#!/usr/bin/env python3

import os
import sys
import glob
import time
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime as dt

tdatetime = dt.now()
todate = tdatetime.strftime('%Y%m%d')
download_directory= '{0}\\{1}'.format(os.getcwd(),todate)

class UseSel(object):
    def __init__(self):
        try:
            os.mkdir(download_directory)
        except:
            pass
        try:
            os.mkdir('{0}\\winpydriver'.format(os.getcwd()))
            print('下記フォルダにWebdriverを配置してください')
            print('{0}\\winpydriver'.format(os.getcwd()))
        except:
            pass
        osver = platform.version().split('.')[0]
        if str(osver) == '10':
            envpath = '{0}\\winpydriver'.format(os.getcwd())
        else:
            envpath = '{0}\\winpydriver_32'.format(os.getcwd())
        orgpath = os.environ['PATH']
        if orgpath.find(envpath) == -1:
            os.environ['PATH'] = '{0};{1}'.format(envpath,orgpath)
            print('Temporary Add a PATHWebdriverの環境変数を一時的に設定しました')
        else:
            pass

    def log(
        self,
        browser='chro',
        width=700,
        height=700,
        **args
    ):
        '''
        Start browser(Default:Google Chrome)
        '''
        try:
            browser = browser.lower()
        except:
            pass
        options = Options()
        osver = platform.version().split('.')[0]
        dpath = '{0}\\winpydriver'.format(os.getcwd())
        try:
            if browser == "ff" or browser == "firefox":
                fp = webdriver.FirefoxProfile()
                fp.set_preference("browser.download.dir", download_directory)
                for i in range(int(len(args)/2)):
                    fp.set_preference(args[i*2],args[i*2+1])
                ffwdpath = "{}\\geckodriver.exe".format(dpath)
                driver = webdriver.Firefox(executable_path=ffwdpath,firefox_profile=fp)
            elif browser == "edge" or browser == "microsoft" or browser == "mse":
                driver = webdriver.Edge("{}\\MicrosoftWebDriver.exe".format(dpath))
            elif browser == "chrome" or browser == "google" or browser == "chro":
                prefs = {"download.default_directory" : download_directory}
                for i in range(int(len(args)/2)):
                    prefs = {args[i*2]:args[i*2+1]}
                options.add_experimental_option("prefs",prefs)
                options.add_argument('--ignore-certificate-errors')
                driver = webdriver.Chrome(executable_path="{}\\chromedriver.exe".format(dpath),chrome_options=options)
            elif browser == "headlesschrome" or browser == "hlc" or browser == "hlchro" or browser == "less":
                browser = "headlesschrome"
                options = Options()
                # Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
                # options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
                # ヘッドレスモードを有効にする
                prefs = {"download.default_directory" : download_directory}
                for i in range(int(len(args)/2)):
                    prefs = {args[i*2]:args[i*2+1]}
                options.add_experimental_option("prefs",prefs)
                options.add_argument('--headless')
                options.add_argument('--allow-insecure-localhost')
                options.add_argument('--ignore-certificate-errors')
                # ChromeのWebDriverオブジェクトを作成する。
                driver = webdriver.Chrome(chrome_options=options,executable_path="{}\\chromedriver.exe".format(dpath))
            elif browser == "ie" or browser == "internetexplorer" or browser == "internet":
                driver = webdriver.Ie("{}\\IEDriverServer.exe".format(dpath))
            else:
                print("Not selected Browser")
                try:
                    print(browser)
                except:
                    pass
                raise Exception
        except:
            print('[ERROR] Check webdriver')
            raise Exception
        if browser != "headlesschrome":
            driver.set_window_position(0,0)
            driver.set_window_size(width,height)
        return driver;

    def get_handle(
        self,
        driver = '',
        num = -1  #  number of WindowHandle
    ):
        '''
        get window handle
        '''
        if num == -1:
            num = len(driver.window_handles) - 1 # latest
        try:
            driver.switch_to_window(driver.window_handles[num])
        except:
            try:
                time.sleep(1)
                driver.switch_to_window(driver.window_handles[-1])
            except:
                pass
        return driver;

    def tryal(
        self,
        key = '',  #  Search keyword
        driver = '',
        method = 'xpath',  #  search method
        num = 3,  #  try count
        action = '', # action e.g( action='send_keys:text' →　send_keys(text) )
        keyword = '',
        keyword2 = '',
        keyword3 = ''
    ):
        '''
        This method repeat to get web element or to perform any actions.
        '''
        reitem = None
        errornum = 0
        while True:
            reitem = ''
            try:
                if method == "class" or method == "class_name" or method == "cn":
                    reitem = driver.find_element_by_class_name(key)
                elif method == "id":
                    reitem = driver.find_element_by_id(key)
                elif method == "name":
                    reitem = driver.find_element_by_name(key)
                elif method == "link_text" or method == "link" or method == "lt":
                    reitem = driver.find_element_by_link_text(key)
                elif method == "partial_link_text":
                    reitem = driver.find_element_by_partial_link_text(key)
                elif method == "tag_name" or method == "tag":
                    reitem = driver.find_element_by_tag_name(key)
                elif method == "xpath":
                    reitem = driver.find_element_by_xpath(key)
                elif method == "css_selector" or method == "css" :
                    reitem = driver.find_element_by_css_selector(key)
                else:
                    print("no such elements")
                try:
                    try:
                        if keyword == '':
                            keyword = action.replace(action.split(':')[0]+':','')
                    except:
                        pass
                    try:
                        if keyword2 == '':
                            keyword2 = action.split(':')[1]
                    except:
                        pass
                    try:
                        if keyword3 == '':
                            keyword3 = action.split(':')[2]
                    except:
                        pass
                    if action.find('click')==0:
                        reitem.click()
                    elif action.find('send_keys')==0 or action.find('sk')==0:
                        reitem.send_keys(keyword)
                    elif action.find('select_by_index')==0 or action.find('sbi')==0:
                        reitem.select_by_index(keyword)
                    elif action.find('select_by_visible_text')==0 or action.find('sbvt')==0:
                        reitem.select_by_visible_text(keyword)
                    elif action.find('deselect_all')==0:
                        reitem.deselect_all()
                    elif action.find('deselect_by_index')==0 or action.find('dbi')==0:
                        reitem.deselect_by_index(keyword)
                    elif action.find('deselect_by_value')==0:
                        reitem.deselect_by_value(keyword)
                    elif action.find('deselect_by_visible_text')==0 or action.find('dbvt')==0:
                        reitem.deselect_by_visible_text(keyword)
                    elif action.find('key_down')==0 or action.find('kd')==0:
                        reitem.key_down(keyword)
                    elif action.find('key_up')==0 or action.find('ku')==0:
                        reitem.key_up(keyword)
                    elif action.find('move_by_offset')==0 or action.find('mbo')==0:
                        reitem.move_by_offset(keyword,keyword2)
                    elif action.find('click_and_hold')==0 or action.find('cah')==0:
                        reitem.click_and_hold(keyword)
                    elif action.find('move_to_element')==0 or action.find('mte')==0:
                        reitem.move_to_element(keyword)
                    elif action.find('drag_and_drop_by_offset')==0 or action.find('dadbo')==0:
                        reitem.drag_and_drop_by_offset(keyword,keyword2,keyword3)
                    elif action.find('drag_and_drop')==0:
                        reitem.drag_and_drop(keyword,keyword2)
                except:
                    pass
                break
            except:
                time.sleep(2)
                errornum += 1
                if errornum > num:
                    raise Exception
        return reitem;

    def nw_tryal(
        self,
            key = '',
            driver = '', 
            method = 'xpath',
            num = 3
            ):
        '''
        change windowhandlw and get web elements
        '''
        reitem = None
        ld = len(driver.window_handles)
        for ijl in range(2):
            try:
                reitem = tryal(key=key,method=method,driver=driver,num=1)
                break
            except:
                for i in range(ld):
                    driver = self.get_handle(driver=driver,num=i)
                    try:
                        reitem = self.tryal(key=key,method=method,driver=driver,num=1)
                        return driver
                    except:
                        pass
                    if i==ld:
                        print('Not found window handle')
                        if ijl == 2:
                            raise Exception
        return driver

    def moveF(
        self,
        iFname = '',  #  name of iFrame (e.g: iFname='a,b,c' )
        driver = '',
        method = 'xpath'
    ):
        '''
        move iframe
        '''
        flist = iFname.split(',')
        try:
            driver.switch_to.default_content()
        except:
            pass
        driver = self.get_handle(
            driver = driver,
            key = flist[0],
            method = method
        )
        driver.switch_to.default_content()
        for flame in flist:
            iframe = self.tryal(
                driver=driver,
                key=flame,
                method=method
            )
            driver.switch_to.frame(iframe)
        return driver;

    def screenshot(
        self,
        driver = '',
        width = 640,
        hight = 640,
        name = 'SS',  #  name of screenshot
        expa = '.png'  #  extention
    ):
        '''
        get screenshot
        '''
        try:
            os.mkdir(todate)
        except:
            pass
        try:
            files = glob.glob(fr'{os.getcwd()}\{todate}\{name}_*.{expa}'))
            if len(files)==0:
                ssnum ="000"
            else:
                latest_num = files[-1].replace(fr"{os.getcwd()}\{todate}\{name}",'').replacer(f".{expa}")
                latest_num = int(latestnum)
                if latest_num == 1000:
                    print("スクリーンショットの取得上限になりました。")
                    raise Exception
                ssnum = str(latestnum + 1).zfill(3)
        except:
            import traceback
            traceback.print_exc()
            ssnum = '000'
        print("Screenshot number:",ssnum)
        Filename = fr'{os.getcwd()}\{todate}\{name}_{ssnum}.{expa}'
        driver.set_window_size(width , hight)
        driver.save_screenshot(Filename)
        return;

    def printhtml(
        self,
        driver = '',
        filename = 'print'  #  fille name
    ):
        '''
        write as html file
        '''
        path = '{}.html'.format(filename)

        with open(path, mode='w', encoding="utf-8") as f:
            f.write(driver.page_source)
        return;
