"""
Main module for patching the sources
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper
from os.path import abspath, dirname, join
from pylib.patching.patchit_file import PatchitFile

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
        self.PatchZlib()
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

    def PatchZlib(self):
        # Copy zlib to the patched directory
        zlibdir = self.copysrctopatched("zlib")

        # Apply patch
        self.log.info("Applying patch zlib-1.2.8-1.patch")
        soxpatchdir = join(self.SrcDir, "sox-" + self.Setts.SoxVersion, "patches")
        patch1 = PatchitFile(join(soxpatchdir, "zlib-1.2.8-1.patch"), self.PatchedDir, 1)
        patch1.Apply()

    # Patch LibSox
    def PatchLibSox(self):
        # Copy sox to the patched directory
        soxdir = self.copysrctopatched("sox")

        # Copy swig .c wrapper into src directory
        self.log.info("Copying swig_wrap.c into sox src directory")
        sox_wrapperfile = abspath(join(self.Setts.DepsDirectory, "sox_swigcsharp", "swig_wrap.c"))
        shutil.copy(sox_wrapperfile, join(soxdir, "src"))

        # Apply patch
        self.log.info("Applying patch libsox-14.4.2-1.patch")
        soxpatchdir = join(self.SrcDir, "sox-" + self.Setts.SoxVersion, "patches")
        patch1 = PatchitFile(join(soxpatchdir, "libsox-14.4.2-1.patch"), self.PatchedDir, 1)
        patch1.Apply()
