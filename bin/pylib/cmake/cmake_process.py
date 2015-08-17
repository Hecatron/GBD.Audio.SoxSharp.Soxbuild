"""
Class for accessing the cmake process
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.process import Process

# Wrapper class for logging
class CMakeProcess(Process):

    def __init__(self):
        super().__init__()
        self.log = LogWrapper.getlogger()

        # CMake Process options
        self.Generator = None
        self.AdditionalOptions = None
        self.SrcDir = None

    def Start(self):
        self.log.info("Starting generation of cmake files")

        # Setup Output directory
        if os.path.exists(self.WorkingDir):
            self.log.warn("Cleaning Output Directory: " + self.WorkingDir)
            shutil.rmtree(self.WorkingDir, ignore_errors=True)
        os.makedirs(self.WorkingDir)

        if self.Options == None: self.Options = []
        self.Options = self.Options + self.GenerateCmdLineOpts()

        self.log.info("CMake: Launching:")
        self.log.info("CMake: Command: " + " ".join(str(x) for x in self.Options))

        super().Start()
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        if self.Generator != None: ret.append("-G" + self.Generator)
        if self.AdditionalOptions != None: ret = ret + self.AdditionalOptions
        if self.SrcDir != None: ret.append(self.SrcDir)
        return ret
