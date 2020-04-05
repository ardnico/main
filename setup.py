#!/usr/bin/env python3

from setuptools import setup
import sys
import os
import os.path
 
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

setup(
    name='useful',
    version='1.0.0',
    description='usuful method for python3',
    install_requires=["pandas", "chardet","selenium"],
    long_description='readme.md',
    author='Masaru Abe',
    author_email='leaf.sun2@gmail.com',
    url='https://qiita.com/mabe',
    license='MIT license'
)