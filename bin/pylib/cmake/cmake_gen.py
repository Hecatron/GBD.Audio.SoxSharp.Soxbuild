"""
Class for generating required cmake files
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.cmake.cmake_process import CMakeProcess
from pylib.depend.depsettings import DependSettings
from os.path import abspath, dirname, join

# Wrapper class for cmake
class CMakeGen(object):

    # Class Constructor
    def __init__(self, Setts):
        self.log = LogWrapper.getlogger()
        self.Setts = Setts

    # Get the generator based on platform
    def getgenerator(self):
        ret = None
        if self.Setts.platform == "Windows":
            ret = "Visual Studio 12 2013"
            # There are currently issues with the newer libs included with VS2015 for libsox
            # http://stackoverflow.com/questions/31150635/build-error-in-visual-studio-in-perlio-h-and-iobuf
            #cmakeproc.Generator = "Visual Studio 14 2015"
        elif self.Setts.platform == "Linux":
            log.error("Not yet implemented")
            sys.exit(1)
        else:
            log.error("Unsupported Platform")
            sys.exit(1)
        return ret

    # Start the CMake Generation
    def Start(self):
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()

        # Run cmake for libsox
        cmakeproc = CMakeProcess()
        cmakeproc.ExePath = "cmake.exe"
        cmakeproc.WorkingDir = join(self.Setts.DepsDirectory, "cmake", "sox")
        cmakeproc.SrcDir = join(self.Setts.DepsDirectory, "packages", "sox")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.Start()
