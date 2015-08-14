#!python3
"""
This script can be used to generate C# Sources from libsox via swig
"""

from scripts.swig_process import SwigProcess
from scripts.script_logs import ScriptLogs
from os.path import abspath, dirname

try:

    # Setup logging
    ScriptLogs.LogLevel = logging.DEBUG
    ScriptLogs.setup()
    log = ScriptLogs.getlogger()

    ROOT = abspath(dirname(__file__))
    osplatform = platform.system()

    # TODO
    swgproc = SwigProcess()


# Output any errors
except Exception as e:
    log.critical (e)
    if ScriptLogs.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)