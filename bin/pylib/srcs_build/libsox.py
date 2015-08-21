"""
LIbsox Handler class
"""

import shutil
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
        self.log = LogWrapper.getlogger()

    def Patch_Srcs(self):
        # Copy sox to the patched directory
        srcdir = self.copysrctopatched("sox")

        # Copy swig .c wrapper into src directory
        self.log.info("Copying swig_wrap.c into sox src directory")
        sox_wrapperfile = abspath(join(self.Setts.DepsDirectory, "sox_swigcsharp", "swig_wrap.c"))
        shutil.copy(sox_wrapperfile, join(srcdir, "src"))

        # Apply patch
        self.log.info("Applying patch libsox-14.4.2-1.patch")
        patch1 = PatchitFile(join(self.Patches_Dir, "libsox-14.4.2-1.patch"), self.Patched_Dir, 1)
        patch1.Apply()

    def Generate_CMake(self):
        # Generate the CMake files
        if self.Setts.CMakeGenerator == None: self.Setts.CMakeGenerator = self.getgenerator()
        cmakeproc = CMakeProcess()
        cmakeproc.WorkingDir = join(self.CmakeBuild_Dir, "sox")
        cmakeproc.SrcDir = join(self.Patched_Dir, "sox")
        cmakeproc.Generator = self.Setts.CMakeGenerator
        cmakeproc.SetupOutputDir()

        # Copy over needed files for cmake
        sox_cmakefile = join(self.Src_Dir, "sox-" + self.Setts.SoxVersion, "cmake", "soxconfig.h.cmake")
        shutil.copy(sox_cmakefile, join(self.CmakeBuild_Dir, "sox"))

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
