"""
Class for accessing the MSBuild process
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.process import Process

# Wrapper class for logging
class MSBuildProcess(Process):

    # Shared Properties

    # Set to "x64" for 64bit, "Win32" for 32bit
    VsPlatform = "Win32"

    # Set to Debug or Release
    VsConfig = "Release"

    # This defaults to Visual Studio 2013
    MSBuildExe = "C:\Program Files (x86)\MSBuild\12.0\Bin\msbuild.exe"

    def __init__(self, solpath):
        super().__init__()
        self.log = LogWrapper.getlogger()

        # Set defaults
        self.SolutionPath = solpath
        self.Target = None
        self.Options = None
        self.AdditionalOptions = None
        self.ExePath = MSBuildProcess.MSBuildExe

    def Start(self):
        self.Options = []
        self.Options = self.Options + self.GenerateCmdLineOpts()
        self.log.info("MSBuild: Launching:")
        self.log.info("MSBuild: Parameters: " + " ".join(str(x) for x in self.Options))
        super().Start()
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        ret.append(self.SolutionPath)
        ret.append("/p:Configuration=" + MSBuildProcess.VsConfig + ";Platform=" + MSBuildProcess.VsPlatform)
        if self.Target != None: ret.append("/t:" + self.Target)
        if self.AdditionalOptions != None: ret = ret + self.AdditionalOptions
        return ret
