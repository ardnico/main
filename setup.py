#!/usr/bin/env python3

from setuptools import setup
import setuptools


from os import path
here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='alittleuseful',
    version='1.0.0',
    author='Masaru Abe',
    author_email='leaf.sun2@gmail.com',
    description='usuful method for python3',
    install_requires=["pandas", "chardet","selenium"],
    long_description=long_description,
    url='https://qiita.com/mabe',
    packages=setuptools.find_packages(),
    license='MIT license',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "read_data = alittleuseful.read_data:read_data",
            "loglotate = alittleuseful.loglotate:loglotate",
            "UseSel = alittleuseful.UseSel:UseSel",
            "ASE_files = alittleuseful.ASE_files:ASE_files"
        ]
    },
    python_requires='>=3.5',
)