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
    VsPlatform_Default = "Win32"

    # Set to Debug or Release
    VsConfig_Default = "Release"

    # This defaults to Visual Studio 2013
    MSBuildExe = "C:\Program Files (x86)\MSBuild\12.0\Bin\msbuild.exe"

    # Class Constructor
    def __init__(self, solpath):
        super().__init__()
        self.log = LogWrapper.getlogger()
        self.Options = None

        # Path to the MSBuild Exe
        self.ExePath = MSBuildProcess.MSBuildExe

        # Configuration to use, e.g. "Release", "Debug"
        self.VsConfig = MSBuildProcess.VsConfig_Default

        # Platform to use, e.g. "Win32", "x64"
        self.VsPlatform = MSBuildProcess.VsPlatform_Default

        # Target defines which project within the solution to build and if to clean / rebuild
        # e.g. "lpc10:Rebuild"
        self.Target = None

        # Build Output Directory
        # see http://www.pseale.com/blog/IHateYouOutDirParameter.aspx
        self.OutDir = None

        # Additional options to be passed to msbuild
        self.AdditionalOptions = None

        # Path to the Solution File
        self.SolutionPath = solpath

    def Start(self, tgt = None):
        if tgt != None: self.Target = tgt
        self.Options = []
        self.Options = self.Options + self.GenerateCmdLineOpts()
        self.log.info("MSBuild: Launching:")
        self.log.info("MSBuild: Parameters: " + " ".join(str(x) for x in self.Options))
        super().Start()
        return

    def CleanOutputDir(self):
        # Setup Output directory
        if os.path.exists(self.OutDir):
            self.log.warn("Cleaning Output Directory: " + self.OutDir)
            shutil.rmtree(self.OutDir, ignore_errors=True)
        os.makedirs(self.OutDir)
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        if self.VsConfig != None: ret.append("/p:Configuration=" + self.VsConfig)
        if self.VsPlatform != None: ret.append("/p:Platform=" + self.VsPlatform)
        if self.Target != None: ret.append("/t:" + self.Target)
        if self.OutDir != None: ret.append("/p:OutDir=" + self.OutDir)
        if self.AdditionalOptions != None: ret = ret + self.AdditionalOptions
        ret.append(self.SolutionPath)
        return ret
