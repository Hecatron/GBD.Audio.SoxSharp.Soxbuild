"""
Class for accessing the swig process
"""

from scripts.script_logs import ScriptLogs

# Wrapper class for logging
class SwigProcess(object):

    def __init__(self):
        self.exepath = ""
        self.log = ScriptLogs.getlogger()

# TODO
