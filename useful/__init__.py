#!/usr/bin/env python3
import sys
import os
 
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

hard_dependencies = ("chardet","pandas")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))


from useful import *
