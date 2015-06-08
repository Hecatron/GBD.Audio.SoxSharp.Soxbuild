

/// <summary> List of common paths / directories. </summary>
public class Paths
{
    #region "General Directories"

    // Paths should be relative to the script location

    /// <summary> Root Directory to store downloaded Archive Files. </summary>
    public static string ArchiveDir = @"..\..\build\archive";

    /// <summary> Root Directory to extract all libsox files into, the main build path. </summary>
    public static string ExtractDir = @"..\..\build\libsoxbuild";

    /// <summary> Root Directory to extract all libsox files into, the main build path. </summary>
    public static string CMakeDir = @"..\..\build\libsoxbuild\cmake";

    #endregion

    #region "Swig Paths"

    /// <summary> Exe used for launching swig. </summary>
    public static string SwigExe = @"..\tools\swig-win\swig.exe";

    /// <summary> Destination Directory for the generation of the swig sources. </summary>
    public static string SwigBuildDir = @"..\..\build\libsoxbuild\sox_swig";

    /// <summary> Root Namespace for the generated swig sources. </summary>
    public static string SwigRootNameSpace = @"GBD.Audio.SoxSharp.Swig";

    /// <summary> Input File used to analyse sources. </summary>
    public static string SwigInputFile = @"..\..\src\sox-14.4.2\swig-win\swig.i";

    #endregion

}

