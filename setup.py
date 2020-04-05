#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

import sys
import os
import os.path
 
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

setup(
    name='useful',
    version='1.0.0',
    description='usuful method for python3',
    install_requires=["pandas", "chardet","selenium"],
    packages=["read_data","UseSel","loglotate"],
    long_description='readme.md',
    author='Masaru Abe',
    author_email='leaf.sun2@gmail.com',
    url='https://qiita.com/mabe',
    license='MIT license',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['read_data = useful.read_data:main',
                            'UseSel = useful.UseSel:main',
                            'loglotate = useful.loglotate:main']
    },
    python_requires='>=3.5',
)