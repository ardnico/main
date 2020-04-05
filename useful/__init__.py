#!/usr/bin/env python3

hard_dependencies = ("chardet","pandas")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))

from useful.read_data import *
from useful.loglotate import *