#!python3
"""
This script can be used to generate C# Sources from libsox via swig
"""

import sys, logging
from pylib.depend.depsettings import DependSettings
from pylib.logwrapper import LogWrapper
from pylib.swig.swig_process import SwigProcess
from os.path import abspath, dirname, join

try:

    # Setup logging
    LogWrapper.LogLevel = logging.DEBUG
    LogWrapper.setup()
    log = LogWrapper.getlogger()

    SoxVersion = "sox-14.4.2"
    ROOT = abspath(dirname(__file__))

    # Load in the Settings from an xml file
    Setts = DependSettings()
    Setts.get_configpath()
    if Setts.ConfigPath == None: sys.exit(1)
    Setts.loadxml()

    # Setup the Swig Process
    swgproc = SwigProcess()
    swgproc.ExePath = join(Setts.DepsDirectory, "packages", "swig", "swig.exe")
    swgproc.WorkingDir = join(Setts.DepsDirectory, "sox_swigcsharp")
    swgproc.Namespace = "GBD.Audio.SoxSharp.Swig"
    swgproc.IncludeDirectories.append(join(Setts.DepsDirectory, "packages", "sox", "src"))
    swgproc.Options.append("-outcurrentdir")
    swgproc.Options.append("-csharp")
    swgproc.InputFile = abspath(join("../src/", SoxVersion, "swig-win", "swig.i"))

    if Setts.platform == "Windows":
        # VS 2013
        swgproc.IncludeDirectories.append("C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\include")
        # VS 2015 - doesn't work?
        #swgproc.IncludeDirectories.append("C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include")

    # Start Generating Swig Source Files
    swgproc.Start();

# Output any errors
except Exception as e:
    log.critical (e)
    if LogWrapper.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
