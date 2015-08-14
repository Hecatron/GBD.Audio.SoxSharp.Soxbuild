#!python3
"""
This script can be used to generate CMake files for libsox
"""

import sys, logging
from scripts.dep_setts import DependSettings
from scripts.script_logs import ScriptLogs
from scripts.cmake_process import CMakeProcess
from os.path import abspath, dirname, join

try:

    # Setup logging
    ScriptLogs.LogLevel = logging.DEBUG
    ScriptLogs.setup()
    log = ScriptLogs.getlogger()

    SoxVersion = "sox-14.4.2"
    ROOT = abspath(dirname(__file__))

    # Load in the Settings from an xml file
    Setts = DependSettings()
    Setts.get_configpath()
    if Setts.ConfigPath == None: sys.exit(1)
    Setts.loadxml()

    # Setup the Swig Process
    cmakeproc = CMakeProcess()
    cmakeproc.ExePath = "cmake.exe"
    cmakeproc.OutputDir = join(Setts.DepsDirectory, "cmake", "sox")
    cmakeproc.SrcDir = join(Setts.DepsDirectory, "packages", "sox")

    if Setts.platform == "Windows":
        cmakeproc.Generator = "Visual Studio 12 2013"
        # There are currently issues with the newer libs included with VS2015 for libsox
        # http://stackoverflow.com/questions/31150635/build-error-in-visual-studio-in-perlio-h-and-iobuf
        #cmakeproc.Generator = "Visual Studio 14 2015"
    elif Setts.platform == "Linux":
        log.error("Not yet implemented")
        sys.exit(1)
    else:
        log.error("Unsupported Platform")
        sys.exit(1)

    # TODO other libs
    # cmakeproc.IncludeDirectories.append("C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\include")

    # Start Generating CMake FIles
    cmakeproc.Start();

# Output any errors
except Exception as e:
    log.critical (e)
    if ScriptLogs.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
