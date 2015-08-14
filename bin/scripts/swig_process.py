"""
Class for accessing the swig process
"""

import shutil, subprocess, os
from scripts.script_logs import ScriptLogs

# Wrapper class for logging
class SwigProcess(object):

    def __init__(self):
        self.log = ScriptLogs.getlogger()

        # Swig Process options
        self.ExePath = None
        self.Namespace = None
        self.SrcDir = None
        self.IncludeDirectories = []
        self.Options = []
        self.InputFile = None
        self.OutputDir = None

    def Start(self):
        self.log.info("Starting generation of swig C# Files")

        # Setup Output directory
        if os.path.exists(self.OutputDir):
            self.log.warn("Cleaning Output Directory: " + self.OutputDir)
            shutil.rmtree(self.OutputDir, ignore_errors=True)
        os.makedirs(self.OutputDir)

        cmdopts = []
        cmdopts.append(self.ExePath)
        cmdopts = cmdopts + self.GenerateCmdLineOpts()

        self.log.info("Swig: Launching:")
        self.log.info("Swig: ExePath: " + self.ExePath)
        self.log.info("Swig: RootNamespace: " + self.Namespace)
        self.log.info("Swig: SrcDir: " + self.SrcDir)
        self.log.info("Swig: Command: " + " ".join(str(x) for x in cmdopts))

        self.run_cmd(cmdopts, self.OutputDir)
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        if self.Options != None: ret = ret + self.Options
        if self.Namespace != None:
            ret.append("-namespace")
            ret.append(self.Namespace)
        for incdir in self.IncludeDirectories:
            ret.append("-I" + incdir)
        if self.InputFile != None: ret.append(self.InputFile)
        return ret

    # Run a command
    def run_cmd(self, cmdarray, workingdir):
        proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        self.log.info(proc_out)
        self.log.warn(proc_err)
        if proc.returncode != 0:
            raise RuntimeError("Failure to run command")
        return
