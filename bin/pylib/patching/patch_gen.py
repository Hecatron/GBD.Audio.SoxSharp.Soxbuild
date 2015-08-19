"""
Main module for patching the sources
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from pylib.cmake.cmake_process import CMakeProcess
from os.path import abspath, dirname, join
from patchit_apply import PatchitApply
#from pylib.patching.patch import fromfile as patch_fromfile

# Wrapper class for patching sources
class PatchGen(object):

    # Class Constructor
    def __init__(self, Setts):
        self.log = LogWrapper.getlogger()
        self.Setts = Setts

        # Directory properties
        self.PackagesDir = abspath(join(self.Setts.DepsDirectory, "packages"))
        self.PatchedDir = abspath(join(self.Setts.DepsDirectory, "patched"))
        self.SrcDir = abspath(join(self.Setts.DepsDirectory, "..", "src"))
        return

    # Start the source patching
    def Start(self):
        self.log.info("Starting to patch sources")
        self.PatchLibSox()
        return

    # Copy Source directory to patch destination
    def copysrctopatched(self, subdir):
        srcdir = join(self.PackagesDir, subdir)
        destdir = join(self.PatchedDir, subdir)
        self.log.info("Copying src " + subdir + " to patched directory")
        if not os.path.exists(self.PackagesDir): os.makedirs(self.PackagesDir)
        if os.path.exists(destdir): shutil.rmtree(destdir, ignore_errors=True)
        shutil.copytree(srcdir, destdir)
        return destdir

    # Patch LibSox
    def PatchLibSox(self):
        # Copy sox to the patched directory
        soxdir = self.copysrctopatched("sox")

        # Copy swig .c wrapper into src directory
        sox_wrapperfile = abspath(join(self.Setts.DepsDirectory, "sox_swigcsharp", "swig_wrap.c"))
        shutil.copy(sox_wrapperfile, join(soxdir, "src"))

        # Apply patch
        soxpatchdir = join(self.SrcDir, "sox-" + self.Setts.SoxVersion, "patches")
        patch1 = PatchitApply(join(soxpatchdir, "swig.patch"), self.PatchedDir, 1)
        patch1.Apply()

        
