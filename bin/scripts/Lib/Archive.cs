using NLog;
using System;
using System.IO;
using System.Reflection;
using ICSharpCode.SharpZipLib.BZip2;
using ICSharpCode.SharpZipLib.GZip;
using ICSharpCode.SharpZipLib.Tar;
using ICSharpCode.SharpZipLib.Zip;
using ICSharpCode.SharpZipLib.LZW;
using SevenZip;

/// <summary> Code for Handling Archives / Compression / Decompression. </summary>
public class Archive
{
    #region "Properties - Static"

    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    /// <summary> Path to the 7Zip Dll. </summary>
    public static string SevenZipDllPath;

    #endregion

    #region "Functions - Static"

    /// <summary> Extracts a file into a Directory using SharpZipLib
    /// attempts to determine the type via file extension. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void Extract(String filepath, String destFolder) {
        string filename = Path.GetFileName(filepath);
        if (String.IsNullOrEmpty(filename)) throw new ArgumentException("File Path Error: " + filepath);
        Logger.Info("Extracting " + filename + " To " + destFolder);
        if (filename.EndsWith(".tar.gz")) ExtractTarGz(filepath, destFolder);
        if (filename.EndsWith(".tar.bz2")) ExtractTarBz2(filepath, destFolder);
        if (filename.EndsWith(".xz")) ExtractTarLzma(filepath, destFolder);
        if (filename.EndsWith(".zip")) ExtractZip(filepath, destFolder);
    }

    /// <summary> Extracts a tar.gz file into a Directory using SharpZipLib. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void ExtractTarGz(String filepath, String destFolder) {
        Stream inStream = File.OpenRead(filepath);
        Stream cmpstream = new GZipInputStream(inStream);
        TarArchive tarArchive = TarArchive.CreateInputTarArchive(cmpstream);
        tarArchive.ExtractContents(destFolder);
        tarArchive.Close();
        cmpstream.Close();
        inStream.Close();
    }

    /// <summary> Extracts a tar.bz2 file into a Directory using SharpZipLib. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void ExtractTarBz2(String filepath, String destFolder) {
        Stream inStream = File.OpenRead(filepath);
        Stream cmpstream = new BZip2InputStream(inStream);
        TarArchive tarArchive = TarArchive.CreateInputTarArchive(cmpstream);
        tarArchive.ExtractContents(destFolder);
        tarArchive.Close();
        cmpstream.Close();
        inStream.Close();
    }

    /// <summary> Extracts a LZW file into a Directory using SharpZipLib. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void ExtractTarLzw(String filepath, String destFolder) {
        Stream inStream = File.OpenRead(filepath);
        Stream cmpstream = new LzwInputStream(inStream);
        TarArchive tarArchive = TarArchive.CreateInputTarArchive(cmpstream);
        tarArchive.ExtractContents(destFolder);
        tarArchive.Close();
        cmpstream.Close();
        inStream.Close();
    }

    /// <summary> Extracts a Lzma (7zip / xz) file into a Directory using SharpZipLib. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void ExtractTarLzma(String filepath, String destFolder) {
        // TODO check this works under Linux / Mono
        Refresh_SevenZipDllPath();

        // Extract to a tar file
        SevenZipExtractor se = new SevenZipExtractor(filepath);
        se.ExtractArchive(destFolder);

        // Extract the tar file
        string tarfile = Path.GetFileNameWithoutExtension(filepath);
        if (string.IsNullOrEmpty(tarfile)) throw new Exception("Tar filename indeterminate");
        string tarpath = Path.Combine(destFolder, tarfile);
        Stream inStream = File.OpenRead(tarpath);
        TarArchive tarArchive = TarArchive.CreateInputTarArchive(inStream);
        tarArchive.ExtractContents(destFolder);
        tarArchive.Close();
        inStream.Close();
        File.Delete(tarpath);
    }

    /// <summary> Set the path to the 7Zip dll. </summary>
    private static void Refresh_SevenZipDllPath() {
        // If we're inside the debugger, use local assembly directory
        if (string.IsNullOrEmpty(SevenZipDllPath))
        {
            SevenZipDllPath = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        }

        // Toggle between the x86 and x64 bit dll
        string dllpath = Path.Combine(SevenZipDllPath, Environment.Is64BitProcess ? "x64" : "x86", "7z.dll");
        SevenZipBase.SetLibraryPath(dllpath);
    }

    /// <summary> Extracts a zip file into a Directory using SharpZipLib. </summary>
    /// <param name="filepath">    Path to the input file to extract. </param>
    /// <param name="destFolder">  Destination directory to extract to. </param>
    public static void ExtractZip(String filepath, String destFolder) {
        FastZip fastzip = new FastZip();
        fastzip.ExtractZip(filepath, destFolder,null);
    }

    #endregion

}
