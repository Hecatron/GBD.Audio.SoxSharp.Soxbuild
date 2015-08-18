#!python3
"""
This script can be used to generate CMake files for libsox
"""

import sys, logging
from pylib.depend.depsettings import DependSettings
from pylib.logwrapper import LogWrapper
from pylib.cmake.cmake_gen import CMakeGen
from pylib.patching.patch_gen import PatchGen
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

    # Start Patching of Sources
    patcher = PatchGen(Setts)
    patcher.Start()

    # Start Generation of cmake files
    generator = CMakeGen(Setts)
    generator.Start()

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
