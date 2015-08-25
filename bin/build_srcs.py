#!python3
"""
This script can be used to generate CMake files for libsox
"""

import sys, logging
from pylib.depend.depsettings import DependSettings
from pylib.logwrapper import LogWrapper
from os.path import abspath, dirname, join
from pylib.subproc.msbuild_process import MSBuildProcess

from pylib.srcs_build.zlib import ZLib
from pylib.srcs_build.libpng import LibPng
from pylib.srcs_build.lame import Lame
from pylib.srcs_build.libsox import Libsox

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

    # Set some default values / shared class properties
    MSBuildProcess.MSBuildExe = join("C:\\", "Program Files (x86)", "MSBuild", "12.0", "Bin", "msbuild.exe")

    #MSBuildProcess.VsConfig_Default = "Debug"
    MSBuildProcess.VsConfig_Default = "Release"

    #Setts.CMakeGenerator = "Visual Studio 12 2013 Win64"
    #MSBuildProcess.VsPlatform_Default = "x64"
    MSBuildProcess.VsPlatform_Default = "Win32"

    # Next lets build some sources
    Builders = []
    #Builders.append(ZLib(Setts))
    #Builders.append(LibPng(Setts))
    Builders.append(Lame(Setts))
    #Builders.append(Libsox(Setts))

    for builditem in Builders:
        builditem.Patch_Srcs()
        builditem.Generate_CMake()
        builditem.MSBuild_Build()

    # TODO As a final step we need to copy out
    # libsox.dll
    # LibMp3Lame.dll
    # LibMad.dll
    # LibSndFile-1.dll

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
