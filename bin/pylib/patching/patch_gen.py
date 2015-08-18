"""
Main module for patching the sources
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.cmake.cmake_process import CMakeProcess
from os.path import abspath, dirname, join

# Wrapper class for patching sources
class PatchGen(object):

    # Class Constructor
    def __init__(self, Setts):
        self.log = LogWrapper.getlogger()
        self.Setts = Setts

    # Start the source patching
    def Start(self):
        self.log.info("Starting to patch sources")



