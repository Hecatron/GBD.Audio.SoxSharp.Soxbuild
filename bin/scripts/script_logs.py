"""
Coloured logging beween modules
"""

import logging, inspect
from colorlog import ColoredFormatter

# Wrapper class for logging
class ScriptLogs(object):

    LogLevel = logging.DEBUG
    LogFormat = None
    LogStream = None

    @staticmethod
    def setup():
        #ScriptLogs.LogFormat = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        ScriptLogs.LogFormat = "%(log_color)s[%(asctime)s]:%(levelname)-7s:%(message)s"
        logging.root.setLevel(ScriptLogs.LogLevel)
        formatter = ColoredFormatter(ScriptLogs.LogFormat)
        ScriptLogs.LogStream = logging.StreamHandler()
        ScriptLogs.LogStream.setLevel(ScriptLogs.LogLevel)
        ScriptLogs.LogStream.setFormatter(formatter)

    @staticmethod
    def getlogger(modname = None):
        if modname == None:
            # Get Calling module name
            frm = inspect.stack()[1]
            modname = inspect.getmodule(frm[0]).__name__

        # Setup Logger
        log = logging.getLogger(modname)
        log.setLevel(ScriptLogs.LogLevel)
        log.addHandler(ScriptLogs.LogStream)
        return log

    @staticmethod
    def testoutput():
        log = ScriptLogs.getlogger()
        log.debug("this is a debugging message")
        log.info("this is an informational message")
        log.warn("this is a warning message")
        log.error("this is an error message")
        log.fatal("this is a fatal message")
        log.critical("this is a critical message")
        return