using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using NLog;

/// <summary> Represents a Swig Process. </summary>
public class SwigProcess
{
    #region "Properties"

    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    /// <summary> Used holding the process start information. </summary>
    private ProcessStartInfo ProcStartinfo;

    /// <summary> Path to the swig exe. </summary>
    public string ExePath;

    /// <summary> Output Directory for built files. </summary>
    public string OutputDir;

    /// <summary> List of include directories for the source code to look at. </summary>
    public List<string> IncludeDirectories;

    /// <summary> Root Namespace to generate the C# Code into. </summary>
    public string NameSpace;

    /// <summary> Input File used to describe which parts of the code to look at. </summary>
    public string InputFile;

    /// <summary> Additional Options. </summary>
    public string Options;

    #endregion

    #region "Constructors"

    /// <summary> Default Constructor. </summary>
    public SwigProcess()
    {
        IncludeDirectories = new List<string>();
    }

    #endregion

    #region "Functions"

    /// <summary> Generate Command Line Options. </summary>
    public string GenerateCmdLineOpts() {
        StringBuilder sb = new StringBuilder();
        foreach (string item in IncludeDirectories) {
            sb.Append(@"-I""" + item + @""" ");
        }
        if (String.IsNullOrEmpty(NameSpace) == false) sb.Append(@"-namespace " + NameSpace + " ");
        if (String.IsNullOrEmpty(Options) == false) sb.Append(Options + " ");
        if (String.IsNullOrEmpty(InputFile) == false) sb.Append(InputFile + " ");
        string cmdopts = sb.ToString();
        return cmdopts;
    }

    /// <summary> Launch Swig. </summary>
    public void Start() {
        if (Directory.Exists(OutputDir) == false) Directory.CreateDirectory(OutputDir);
        ProcStartinfo = new ProcessStartInfo {
            FileName = ExePath,
            WorkingDirectory = OutputDir,
            Arguments = GenerateCmdLineOpts(),
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false
        };
        Logger.Info("Launching swig:");
        Logger.Info("Swig: Exe Path= " + ExePath);
        Logger.Info("Swig: Working Directory= " + OutputDir);
        Logger.Info("Swig: Arguments= " + ProcStartinfo.Arguments);
        var proc1 = Process.Start(ProcStartinfo);
        if (proc1 == null) throw new Exception("Process Launch Error");
        Logger.Info(proc1.StandardOutput.ReadToEnd());
        Logger.Error(proc1.StandardError.ReadToEnd());
        proc1.WaitForExit();
    }

    #endregion

}
