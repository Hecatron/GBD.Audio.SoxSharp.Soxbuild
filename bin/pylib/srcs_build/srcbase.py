
"""
Src Package Base class
"""

import shutil, os
from pylib.logwrapper import LogWrapper
from pylib.subproc.msbuild_process import MSBuildProcess
from os.path import abspath, dirname, join

# Base Class for package modules
class SrcBase(object):

    # Class Constructor
    def __init__(self, Setts):
        self.log = LogWrapper.getlogger()
        self.Setts = Setts
        self.CmakeBuild_Dir = join(Setts.DepsDirectory, "cmake")
        self.Src_Dir = abspath(join(self.Setts.DepsDirectory, "..", "src"))
        self.Packages_Dir = abspath(join(self.Setts.DepsDirectory, "packages"))
        self.Patched_Dir = abspath(join(self.Setts.DepsDirectory, "patched"))

    # Get the generator based on platform
    def getgenerator(self):
        ret = None
        if self.Setts.platform == "Windows":
            ret = "Visual Studio 12 2013"
            # There are currently issues with the newer libs included with VS2015 for libsox
            # http://stackoverflow.com/questions/31150635/build-error-in-visual-studio-in-perlio-h-and-iobuf
            #cmakeproc.Generator = "Visual Studio 14 2015"
        elif self.Setts.platform == "Linux":
            self.log.error("Not yet implemented")
            sys.exit(1)
        else:
            self.log.error("Unsupported Platform")
            sys.exit(1)
        return ret

    # Copy Source directory to patch destination
    def copysrctopatched(self, subdir):
        srcdir = join(self.Packages_Dir, subdir)
        destdir = join(self.Patched_Dir, subdir)
        self.log.info("Copying src " + subdir + " to patched directory")
        if not os.path.exists(self.Patched_Dir): os.makedirs(self.Patched_Dir)
        if os.path.exists(destdir): shutil.rmtree(destdir, ignore_errors=True)
        shutil.copytree(srcdir, destdir)
        return destdir
