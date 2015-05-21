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
        //var deps = GetDepends();
        //DownloadExtractDepends(deps);
    }

    #endregion

}
