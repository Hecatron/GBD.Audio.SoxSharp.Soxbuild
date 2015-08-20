"""
LibPng Handler class
"""

import shutil
from pylib.logwrapper import LogWrapper
from pylib.srcs_build.srcbase import SrcBase
from pylib.patching.patchit_file import PatchitFile
from pylib.subproc.cmake_process import CMakeProcess
from pylib.subproc.msbuild_process import MSBuildProcess
from os.path import abspath, join

# Wrapper class for ZLib
class LibPng(SrcBase):

    # Class Constructor
    def __init__(self, Setts):
        super().__init__(Setts)
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy libpng to the patched directory
        # TODO
        #srcdir = self.copysrctopatched("libpng")
        print("TODO")

    def Generate_CMake(self):
        # Generate the CMake files
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "libpng")
        cmakeproc.SrcDir = join(self.Patched_Dir, "libpng")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()
        cmakeproc.Start()

    def MSBuild_Build(self):
        # Build the sources using msbuild
        print("TODO")
        #msbuildproc = MSBuildProcess(join(self.CmakeBuild_Dir, "libpng", "libpng.sln"))
        #msbuildproc.Start(tgt = "libpng:Clean")
        #msbuildproc.Start(tgt = "libpng:Rebuild")
