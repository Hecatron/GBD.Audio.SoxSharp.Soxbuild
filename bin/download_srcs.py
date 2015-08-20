#!python3
"""
This script can be used to download depends required for cmake mbed
"""

import sys, logging
from pylib.depend.depsettings import DependSettings
from pylib.logwrapper import LogWrapper
from os.path import abspath, dirname

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

    # Download and Extract all sources
    Setts.getdeps()
    
    # Depends Setup Complete
    log.info("Download of Depends Complete")

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
