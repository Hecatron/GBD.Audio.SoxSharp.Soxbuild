#!python3
"""
This script is just a shortcut to building all the required libs via msbuild / visual studio environment
"""

import sys, logging
from pylib.depend.depsettings import DependSettings
from pylib.logwrapper import LogWrapper
from pylib.cmake.msbuild_process import MSBuildProcess
from os.path import abspath, dirname, join

try:

    # Setup logging
    LogWrapper.LogLevel = logging.DEBUG
    LogWrapper.setup()
    log = LogWrapper.getlogger()

    ROOT = abspath(dirname(__file__))

    # Load in the Settings from an xml file
    Setts = DependSettings()
    Setts.get_configpath()
    if Setts.ConfigPath == None: sys.exit(1)
    Setts.loadxml()

    cmakebuild_dir = join(Setts.DepsDirectory, "cmake")
    MSBuildProcess.MSBuildExe = join("C:\\", "Program Files (x86)", "MSBuild", "12.0", "Bin", "msbuild.exe")
    #MSBuildProcess.VsConfig = "Debug"
    MSBuildProcess.VsConfig = "Release"
    #MSBuildProcess.VsPlatform = "x64"
    MSBuildProcess.VsPlatform = "Win32"

    # Build libsox
    msbuildproc = MSBuildProcess(join(cmakebuild_dir, "sox", "sox.sln"))
    msbuildproc.Start(tgt = "gsm:Clean")
    msbuildproc.Start(tgt = "gsm:Rebuild")
    msbuildproc.Start(tgt = "lpc10:Clean")
    msbuildproc.Start(tgt = "lpc10:Rebuild")
    msbuildproc.Start(tgt = "libsox:Clean")
    msbuildproc.Start(tgt = "libsox:Rebuild")

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
