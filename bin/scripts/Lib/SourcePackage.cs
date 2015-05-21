using NLog;
using System;
using System.IO;
using System.Net;

/// <summary> Code for Handling Source Code Packages</summary>
[Serializable]
public class SourcePackage
{
    #region "Properties - Static"

    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    /// <summary> Root Directory for downloading archive files to. </summary>
    public static string RootArchiveDir { get; set; }

    /// <summary> Root Directory for extracting sources to. </summary>
    public static string RootExtractDir { get; set; }

    #endregion

    #region "Properties"

    /// <summary> The Name of the Dependency. </summary>
    public string Name { get; set; }

    /// <summary> The Version of the Dependency. </summary>
    public string Version { get; set; }

    /// <summary> The FileName of the downloaded Dependency. </summary>
    public string FileName { get; set; }

    /// <summary> Extraction SubDirectory. </summary>
    public string ExtractSubDir { get; set; }

    /// <summary> The Download Url of the Dependency. </summary>
    public string DownloadUrl { get; set; }

    #endregion

    #region "Constructors"

    /// <summary> Default constructor. </summary>
    public SourcePackage() { 
    }

    /// <summary> Depend Constructor. </summary>
    /// <param name="name">         The name of the depend used for directory paths. </param>
    /// <param name="version">      The version of the depend for downloads. </param>
    /// <param name="filename">     Filename of the downloaded file to be used for extraction. </param>
    /// <param name="extractsubdir"> The extraction sub directory. </param>
    /// <param name="downloadurl">  The downloadurl path to download the depend. </param>
    public SourcePackage(string name, string version, string filename, string extractsubdir, string downloadurl)
    {
        Name = name;
        Version = version;
        FileName = filename;
        ExtractSubDir = extractsubdir;
        DownloadUrl = downloadurl;
    }

    #endregion

    #region "Functions - Property Substitution"

    /// <summary> Download Url with Name / Version replaced. </summary>
    public string DownloadUrl_Formatted() {
        return DownloadUrl.Replace("{Version}", Version).Replace("{Name}", Name);
    }

    /// <summary> FileName with Name / Version replaced. </summary>
    public string FileName_Formatted() {
        return FileName.Replace("{Version}", Version).Replace("{Name}", Name);
    }

    /// <summary> Full path to the archive file. </summary>
    public string FilePath_Formatted() {
        return Path.Combine(RootArchiveDir, FileName_Formatted());
    }

    /// <summary> ExtractSubDir with Name / Version replaced. </summary>
    public string ExtractSubDir_Formatted() {
        return ExtractSubDir.Replace("{Version}", Version).Replace("{Name}", Name);
    }

    #endregion

    #region "Functions"

    /// <summary> Http Download the Depend. </summary>
    public void HttpDownload() {
        using (var client = new WebClient()) {
            string downloadpath = FilePath_Formatted();
            if (File.Exists(downloadpath)) {
                Logger.Warn("File already downloaded, skipping: " + FileName_Formatted());
                return;
            }
            Logger.Info("Downloading " + DownloadUrl_Formatted() + " To " + downloadpath);
            client.DownloadFile(DownloadUrl_Formatted(), downloadpath);
        }
    }

    /// <summary> Extracts the depend. </summary>
    public void Extract() {
        Archive.Extract(FilePath_Formatted(), RootExtractDir);
        string src = Path.Combine(RootExtractDir, Name + "-" + Version);
        string dest = Path.Combine(RootExtractDir, ExtractSubDir_Formatted());
        Directory.Move(src, dest);
    }

    /// <summary> Checks if the Depend has already been extracted. </summary>
    public bool ExtractDirExists() {
        string extractdir = RootExtractDir;
        if (!String.IsNullOrEmpty(ExtractSubDir)) extractdir = Path.Combine(extractdir, ExtractSubDir_Formatted());
        if (Directory.Exists(extractdir)) return true;
        return false;
    }

    #endregion



}
