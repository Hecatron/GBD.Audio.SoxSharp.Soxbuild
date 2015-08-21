"""
Lame Handler class
"""

import shutil
from pylib.logwrapper import LogWrapper
from pylib.srcs_build.srcbase import SrcBase
from pylib.patching.patchit_file import PatchitFile
from pylib.subproc.cmake_process import CMakeProcess
from pylib.subproc.msbuild_process import MSBuildProcess
from os.path import abspath, join

# Wrapper class for ZLib
class Lame(SrcBase):

    # Class Constructor
    def __init__(self, Setts):
        super().__init__(Setts)
        self.Patches_Dir = join(self.Src_Dir, "lame-3.99.5", "patches")
        self.ModifiedSrc_Dir = join(self.Src_Dir, "lame-3.99.5", "modifiedsrc")
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy lame to the patched directory
        #srcdir = self.copysrctopatched("lame")

        # Copy over modified CmakeLists.txt file / config.h
        #shutil.copy(join(self.ModifiedSrc_Dir, "libmp3lame", "CMakeLists.txt"), join(srcdir, "libmp3lame"))
        #shutil.copy(join(self.ModifiedSrc_Dir, "libmp3lame", "config.h"), join(srcdir, "libmp3lame"))

        print("TODO PATCH")


    def Generate_CMake(self):
        # Generate the CMake files
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "libmp3lame")
        cmakeproc.SrcDir = join(self.Patched_Dir, "lame", "libmp3lame")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()
        cmakeproc.Start()

    def MSBuild_Build(self):
        # Build the sources using msbuild
        msbuildproc = MSBuildProcess(join(self.CmakeBuild_Dir, "libmp3lame", "lame.sln"))
        #msbuildproc.Start(tgt = "LibMp3Lame:Clean")
        #msbuildproc.Start(tgt = "LibMp3Lame:Rebuild")
