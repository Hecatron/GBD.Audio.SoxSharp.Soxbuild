"""
General Process wrapper script
"""

import shutil, subprocess, os
from pylib.logwrapper import LogWrapper

# Wrapper class for logging
class Process(object):

    def __init__(self):
        self.log = LogWrapper.getlogger()

        # Process options
        self.ExePath = None
        self.WorkingDir = None
        self.Options = []
        
    def Start(self):

        # Set the Working directory to the current one if not specified
        if self.WorkingDir == None: self.WorkingDir = "."
        if self.ExePath == None:
            raise ValueError("ExePath not specified")

        cmdopts = []
        cmdopts.append(self.ExePath)
        if self.Options != None: cmdopts = cmdopts + self.Options
        self.run_cmd(cmdopts, self.WorkingDir)
        return

    # Run a command
    def run_cmd(self, cmdarray, workingdir):
        proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        self.log.info(proc_out)
        self.log.warn(proc_err)
        if proc.returncode != 0:
            raise RuntimeError("Failure to run command")
        return
