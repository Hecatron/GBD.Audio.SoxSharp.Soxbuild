"""
Class for accessing the swig process
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.process import Process

# Wrapper class for logging
class SwigProcess(Process):

    def __init__(self):
        super().__init__()
        self.log = LogWrapper.getlogger()

        # Swig Process options
        self.Namespace = None
        self.IncludeDirectories = []
        self.InputFile = None

    def Start(self):
        self.log.info("Starting generation of swig C# files")

        # Setup Output directory
        if os.path.exists(self.WorkingDir):
            self.log.warn("Cleaning Output Directory: " + self.WorkingDir)
            shutil.rmtree(self.WorkingDir, ignore_errors=True)
        os.makedirs(self.WorkingDir)

        if self.Options == None: self.Options = []
        self.Options = self.Options + self.GenerateCmdLineOpts()

        self.log.info("Swig: Launching:")
        self.log.info("Swig: ExePath: " + self.ExePath)
        self.log.info("Swig: RootNamespace: " + self.Namespace)
        self.log.info("Swig: Command: " + " ".join(str(x) for x in self.Options))
        super().Start()
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        if self.Namespace != None:
            ret.append("-namespace")
            ret.append(self.Namespace)
        for incdir in self.IncludeDirectories:
            ret.append("-I" + incdir)
        if self.InputFile != None: ret.append(self.InputFile)
        return ret
