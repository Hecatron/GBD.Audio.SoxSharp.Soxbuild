"""
LIbsox Handler class
"""

import shutil, os
from pylib.logwrapper import LogWrapper
from pylib.srcs_build.srcbase import SrcBase
from pylib.patching.patchit_file import PatchitFile
from pylib.subproc.cmake_process import CMakeProcess
from pylib.subproc.msbuild_process import MSBuildProcess
from os.path import abspath, join

# Wrapper class for ZLib
class Libsox(SrcBase):

    # Class Constructor
    def __init__(self, Setts):
        super().__init__(Setts)
        self.Patches_Dir = join(self.Src_Dir, "sox-" + self.Setts.SoxVersion, "patches")
        self.ModifiedSrc_Dir = join(self.Src_Dir, "sox-" + self.Setts.SoxVersion, "modifiedsrc")
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy sox to the patched directory
        srcdir = self.copysrctopatched("sox")

        # Copy swig .c wrapper into src directory
        self.log.info("Copying swig_wrap.c into sox src directory")
        sox_wrapperfile = abspath(join(self.Setts.DepsDirectory, "sox_swigcsharp", "swig_wrap.c"))
        shutil.copy(sox_wrapperfile, join(srcdir, "src"))

        # Copy over the file that determines which libs libsox will look for
        sox_cmakefile = join(self.Src_Dir, "sox-" + self.Setts.SoxVersion, "cmake", "soxconfig.h.cmake")
        shutil.copy(sox_cmakefile, join(srcdir, "src"))

        # Copy over modified CmakeLists.txt files
        shutil.copy(join(self.ModifiedSrc_Dir, "libgsm", "CMakeLists.txt"), join(srcdir, "libgsm"))
        shutil.copy(join(self.ModifiedSrc_Dir, "lpc10", "CMakeLists.txt"), join(srcdir, "lpc10"))
        shutil.copy(join(self.ModifiedSrc_Dir, "src", "CMakeLists.txt"), join(srcdir, "src"))

    def Generate_CMake(self):
        # Generate the CMake files
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "sox")
        cmakeproc.SrcDir = join(self.Patched_Dir, "sox")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()
        cmakeproc.Start()

    def MSBuild_Build(self):
        # Build the sources using msbuild
        msbuildproc = MSBuildProcess(join(self.CmakeBuild_Dir, "sox", "sox.sln"))
        msbuildproc.Start(tgt = "gsm:Clean")
        msbuildproc.Start(tgt = "gsm:Rebuild")
        msbuildproc.Start(tgt = "lpc10:Clean")
        msbuildproc.Start(tgt = "lpc10:Rebuild")
        msbuildproc.Start(tgt = "libsox:Clean")
        msbuildproc.Start(tgt = "libsox:Rebuild")
