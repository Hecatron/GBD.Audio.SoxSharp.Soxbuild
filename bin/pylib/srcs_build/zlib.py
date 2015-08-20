"""
Zlib Handler class
"""

import shutil
from pylib.logwrapper import LogWrapper
from pylib.srcs_build.srcbase import SrcBase
from pylib.patching.patchit_file import PatchitFile
from pylib.subproc.cmake_process import CMakeProcess
from pylib.subproc.msbuild_process import MSBuildProcess
from os.path import abspath, join

# Wrapper class for ZLib
class ZLib(SrcBase):

    # Class Constructor
    def __init__(self, Setts):
        super().__init__(Setts)
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy zlib to the patched directory
        srcdir = self.copysrctopatched("zlib")

        # Apply patch
        self.log.info("Applying patch zlib-1.2.8-1.patch")
        patch1 = PatchitFile(join(self.Patches_Dir, "zlib-1.2.8-1.patch"), self.Patched_Dir, 1)
        patch1.Apply()

    def Generate_CMake(self):
        # Generate the CMake files
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "zlib")
        cmakeproc.SrcDir = join(self.Patched_Dir, "zlib")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()
        cmakeproc.Start()

    def MSBuild_Build(self):
        # Build the sources using msbuild
        msbuildproc = MSBuildProcess(join(self.CmakeBuild_Dir, "zlib", "zlib.sln"))
        msbuildproc.Start(tgt = "zlib:Clean")
        msbuildproc.Start(tgt = "zlib:Rebuild")
