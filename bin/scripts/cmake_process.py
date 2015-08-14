"""
Class for accessing the cmake process
"""

import shutil, subprocess, os
from scripts.script_logs import ScriptLogs

# Wrapper class for logging
class CMakeProcess(object):

    def __init__(self):
        self.log = ScriptLogs.getlogger()

        # CMake Process options
        self.ExePath = None
        self.OutputDir = None
        self.Generator = None
        self.SrcDir = None
        self.AdditionalOptions = None
        
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

        self.log.info("CMake: Launching:")
        self.log.info("CMake: Command: " + " ".join(str(x) for x in cmdopts))

        self.run_cmd(cmdopts, self.OutputDir)
        return

    # Generate Command Line Options
    def GenerateCmdLineOpts(self):
        ret = []
        if self.Generator != None: ret.append("-G" + self.Generator)
        if self.AdditionalOptions != None: ret = ret + self.AdditionalOptions
        if self.SrcDir != None: ret.append(self.SrcDir)


        #for incdir in self.IncludeDirectories:
        #    ret.append("-I" + incdir)
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
