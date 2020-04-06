#!/usr/bin/env python3

from setuptools import setup
import setuptools
import sys
import os
import os.path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='useful',
    version='1.0.0',
    author='Masaru Abe',
    author_email='leaf.sun2@gmail.com',
    description='usuful method for python3',
    install_requires=["pandas", "chardet","selenium","Crypto"],
    long_description='readme.md',
    url='https://qiita.com/mabe',
    packages=setuptools.find_packages(),
    license='MIT license',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)