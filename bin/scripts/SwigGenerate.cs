using System.IO;
using NLog;

/// <summary> HttpDownload LibSox Sources Code. </summary>
public class SwigGenerate
{
    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    #region "Functions"

    /// <summary> Main entry-point for this application. </summary>
    /// <param name="args"> Array of command-line argument strings. </param>
    public static void Main(string[] args)
    {
        Logger.Info("Starting Generation of Swig Files");

        SwigProcess swigproc = new SwigProcess();
        swigproc.ExePath = GlobalScript.AbsPath(Paths.SwigExe);
        swigproc.NameSpace = Paths.SwigRootNameSpace;
        string sox_srcdir = Path.Combine(GlobalScript.AbsPath(Paths.ExtractDir), @"sox\src");
        swigproc.IncludeDirectories.Add(sox_srcdir);
        swigproc.Options = @"-csharp";
        swigproc.InputFile = GlobalScript.AbsPath(Paths.SwigInputFile);
        swigproc.OutputDir = GlobalScript.AbsPath(Paths.SwigBuildDir);

        // TODO Check if platform is windows, and check Visual Studio version - assuming 2013
        swigproc.IncludeDirectories.Add(@"C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\include");

        // Start Generating Swig Source Files
        swigproc.Start();
    }

    #endregion

}
