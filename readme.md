alittleuseful
====

this library offer a little useful methods for python3.

## Description

1. read_data :  This method will detect file's Character codes and
                return dataframes. 
                Currently you can specify such arguments(skiprows,dtype,sep)

2. loglotate :  This class treat log files and circulate logfiles 
                by file size and number of files.And This method can write
                into some logfiles that you specified.

3. UseSel :     Because Selenium sometimes try to catch any web elements
                before completing to load web page and fails,
                this method prepared a method that repeat to try to catch
                any web elements.

4. ASE_files :  This method can encrypt any keywords and decrypt keywords.

## Requirement

pandas,selenium,chardet,Crypto

## Usage

    from alittleuseful import read_data
    # read csv or excel data as dataframe
    dataframe = read_data(filepath[,skiprows=0][,dtype='str'][,sep=','])

    from alittleuseful import loglotate
    # declare a class and circulate logfiles
    logger = loglotate(logname:str='logfile',outputdir:list=[current_directory],
                        [firsttext:str = '[INFO]<filename> started by <hostname>', ]
                        [lsize:int=100000, ]
                        [num:int=20, ]
                        [timestanp:int = 1 # 1:on other:off] )
    # write into logfile 
    logger.write(text:str='',[logdir:list=[]])

    from alittle import UseSel
    # class web driver(lounch web browser)
    driver = UseSel.log(browser='chrome',[width=700,][height=700,][**args])
    # catch specific window handles(Default : lateest)
    driver = UseSel.get_handle(
                        driver = driver,
                        [num = -1  #  number of WindowHandle ]
                    )
    # repeat to try to catch any web elements(and to action)
    webelement = UseSel.tryal(
                        key = '',  #  Search keyword
                        driver = driver,
                        [method = 'xpath',  #  search method ]
                        [num = 3,  #  try count ]
                        [action = '', # action e.g( action='send_keys:text' →　send_keys(text) ) ]
                        [keyword = '', ]
                        [keyword2 = '', ]
                        [keyword3 = '' ]
                    )
    # repeat to try to catch any web elements and change window handles 
    webelement = UseSel.nw_tryal(
                        key = '',
                        driver = driver,
                        [method = 'xpath', ]
                        [num = 3 ]
                    )
    # catch iframe web handle
    driver = UseSel.moveF(
                        driver = driver,
                        iFname = '',  #  name of iFrame (e.g: iFname='a,b,c' )
                        [method = 'xpath' ]
                    )
    # get a screenshot
    UseSel.screenshot(
                        driver = driver,
                        [width = 640, ]
                        [hight = 640, ]
                        [name = 'SS',  #  name of screenshot ]
                        [expa = '.png'  #  extention ]
                    )
    # get a html file
    UseSel.printhtml(
                        driver = driver,
                        [filename = 'print'  #  fille name ]
                    )

    from alittleuseful import ASE_files as ase
    # encrypt any keyword
    ase.encryption(filename,keyword)

    # decrypt encrypted files by this library
    ase.decription(filename)

    # delete encrypted files by this library
    ase.dell_enc_data(filename)

## Install

pip install git+https://github.com/ardnico/main

## Contribution

1. Fork it ( http://github.com//ardnico/main )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence

ALittleUseful

Copyright (c) 2020/04 Ardnico

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php

## Author

[nico](https://qiita.com/mabe)
