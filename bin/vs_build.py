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
    #MSBuildProcess.VsConfig_Default = "Debug"
    MSBuildProcess.VsConfig_Default = "Release"
    #MSBuildProcess.VsPlatform_Default = "x64"
    MSBuildProcess.VsPlatform_Default = "Win32"

    # Build libsox
    msbuildproc = MSBuildProcess(join(cmakebuild_dir, "sox", "sox.sln"))
    msbuildproc.Start(tgt = "gsm:Clean")
    msbuildproc.Start(tgt = "gsm:Rebuild")
    msbuildproc.Start(tgt = "lpc10:Clean")
    msbuildproc.Start(tgt = "lpc10:Rebuild")
    msbuildproc.Start(tgt = "libsox:Clean")
    msbuildproc.Start(tgt = "libsox:Rebuild")

    # Notes
    # 1. For the Output directory it's best to set this at the cmake level
    # https://cognitivewaves.wordpress.com/cmake-and-visual-studio/
    # http://stackoverflow.com/questions/6594796/how-do-i-make-cmake-output-into-a-bin-dir

    # 2. For the Directories to search for lib files again it's best to set this at the cmake level
    # AdditionalLibPaths doesn't seem to get passed to the linker with msbuild for some reason
    # envariables can be set as a work around
    # http://stackoverflow.com/questions/15654002/adding-additional-library-and-include-paths-when-compiling-from-command-line
    # But again it's best to this at the cmake level so that the project files are setup with the paths instead

    # 3. For additional output from msbuild try:
    # try /v:diagnostic

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
