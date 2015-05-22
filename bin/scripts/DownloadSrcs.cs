using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Linq;
using NLog;

/// <summary> Http Download LibSox Source Code. </summary>
class DownloadSrcs
{
    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    #region "Functions"

    /// <summary> Main entry-point for this application. </summary>
    /// <param name="args"> Array of command-line argument strings. </param>
    public static void Main(string[] args)
    {
        Logger.Info("Starting Download / Extraction of Sources");
        var deps = GetDepends();
        DownloadExtractDepends(deps);
    }

    /// <summary> HttpDownload and Extract all Dependencies. </summary>
    public static void DownloadExtractDepends(List<SourcePackage> deps)
    {
        string archiveDirAbs = GlobalScript.AbsPath(Paths.ArchiveDir);
        string extractDirAbs = GlobalScript.AbsPath(Paths.ExtractDir);

        if (Directory.Exists(archiveDirAbs) == false) Directory.CreateDirectory(archiveDirAbs);
        if (Directory.Exists(extractDirAbs) == false) Directory.CreateDirectory(extractDirAbs);
        SourcePackage.ArchiveDir = archiveDirAbs;
        SourcePackage.ExtractDir = extractDirAbs;

        foreach (SourcePackage item in deps)
        {
            Logger.Info("Parsing: " + item.Name);
            if (item.ExtractDirExists()) {
                Logger.Warn("Skipping Directory already exists: " + item.Name);
                continue;
            }
            item.HttpDownload();
            
            switch (item.Name) {

                case "wavpack":
                    //TODO see if this is different under Linux
                    string wavpackdir = Path.Combine(extractDirAbs, item.ExtractSubDir_Formatted());
                    Directory.CreateDirectory(wavpackdir);
                    Archive.Extract(item.FilePath_Formatted(), wavpackdir);
                    break;

                default:
                    item.Extract();
                    break;
            }
        }
    }

    /// <summary> List of Depend Names / Paths. </summary>
    public static List<SourcePackage> GetDepends()
    {
        string srcspath = Path.Combine(GlobalScript.ScriptRunLocation(), "Sources.xml");
        XElement xelement = XElement.Load(srcspath);
        List<SourcePackage> ret = SourcePackage.Deserialize_List(xelement);
        //string srcstxt = File.ReadAllText(srcspath);
        //List<SourcePackage> ret = XmlSerial<SourcePackage>.Deserialize_List(srcstxt);

        // Handle wavpac since it has different sources for windows / unix
        var wplin = (from item in ret where item.Name == "wavpack-linux" select item).FirstOrDefault();
        var wpwin = (from item in ret where item.Name == "wavpack-win" select item).FirstOrDefault();
        if (GlobalScript.IsOsUnix())
        {
            if (wpwin != null) ret.Remove(wpwin);
            if (wplin != null) wplin.Name = "wavpack";
        }
        else
        {
            if (wplin != null) ret.Remove(wplin);
            if (wpwin != null) wpwin.Name = "wavpack";
        }
        return ret;
    }

    #endregion

}
