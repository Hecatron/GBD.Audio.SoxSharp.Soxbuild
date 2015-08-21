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
        self.Patches_Dir = join(self.Src_Dir, "libpng-1.6.18", "patches")
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy libpng to the patched directory
        srcdir = self.copysrctopatched("libpng")

        # Apply patch
        self.log.info("Applying patch libpng-1.6.18-1.patch")
        patch1 = PatchitFile(join(self.Patches_Dir, "libpng-1.6.18-1.patch"), self.Patched_Dir, 1)
        patch1.Apply()

    def Generate_CMake(self):
        # Generate the CMake files

        # TODO can we have multiple directories within ZLIB_ROOT?
        # https://github.com/Kitware/CMake/blob/master/Modules/FindZLIB.cmake
        #set(ZLIB_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../zlib")
        #Could NOT find ZLIB (missing: ZLIB_LIBRARY)

        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "libpng")
        cmakeproc.SrcDir = join(self.Patched_Dir, "libpng")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()
        cmakeproc.Start()

    def MSBuild_Build(self):
        # Build the sources using msbuild
        msbuildproc = MSBuildProcess(join(self.CmakeBuild_Dir, "libpng", "libpng.sln"))
        msbuildproc.Start(tgt = "png16:Clean")
        msbuildproc.Start(tgt = "png16:Rebuild")
