using System.Diagnostics;
using System.IO;
using NLog;

/// <summary> HttpDownload LibSox Sources Code. </summary>
public class CMakeGenerate
{
    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    #region "Functions"

    /// <summary> Main entry-point for this application. </summary>
    /// <param name="args"> Array of command-line argument strings. </param>
    public static void Main(string[] args)
    {
        Logger.Info("Starting Generation of CMake Files");

        // Generate CMake for libsox
        string sox_dir = Path.Combine(GlobalScript.AbsPath(Paths.ExtractDir), "sox");
        string sox_cmakedir = Path.Combine(GlobalScript.AbsPath(Paths.CMakeDir),"sox");
        if (!Directory.Exists(sox_cmakedir)) Directory.CreateDirectory(sox_cmakedir);

        // TODO Pass in parameters, remove the Visual Studio 2013 reference
        // TODO Do a better job of representing this in a class

        ProcessStartInfo info = new ProcessStartInfo();
        info.FileName = "cmake";
        info.WorkingDirectory = sox_cmakedir;
        info.Arguments = @"-G """"Visual Studio 12 2013"""" " + sox_dir;
        var procmakeSoxProc = Process.Start(info);
        if (procmakeSoxProc != null) procmakeSoxProc.WaitForExit();

        // TODO
    }

    #endregion

}
