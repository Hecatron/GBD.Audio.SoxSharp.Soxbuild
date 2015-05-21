using System.Collections.Generic;
using System.IO;
using NLog;

/// <summary> HttpDownload LibSox Sources Code. </summary>
class DownloadSrcs
{
    #region "Properties"

    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    /// <summary> Root Directory to store downloaded Archive Files. </summary>
    public static string RootArchiveDir = @"..\build\archive";

    /// <summary> Root Directory to extract all libsox files into, the main build path. </summary>
    public static string RootExtractDir = @"..\build\libsoxbuild";

    #endregion

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
        if (Directory.Exists(RootArchiveDir) == false) Directory.CreateDirectory(RootArchiveDir);
        if (Directory.Exists(RootExtractDir) == false) Directory.CreateDirectory(RootExtractDir);
        SourcePackage.RootArchiveDir = RootArchiveDir;
        SourcePackage.RootExtractDir = RootExtractDir;

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
                    string wavpackdir = Path.Combine(RootExtractDir, item.ExtractSubDir_Formatted());
                    Directory.CreateDirectory(wavpackdir);
                    Archive.Extract(item.FilePath_Formatted(), wavpackdir);
                    break;

                default:
                    item.Extract();
                    break;


            }

        }
    }

    //TODO Switch around once we get a reply from scriptcs

    ///// <summary> List of Depend Names / Paths. </summary>
    //public static List<SourcePackage> GetDepends() {
    //    string srcspath = Path.Combine(GlobalScript.ScriptRunLocation(), "Sources.xml");
    //    string srcstxt = File.ReadAllText(srcspath);
    //    List<SourcePackage> ret = XmlSerial<SourcePackage>.Deserialize_List(srcstxt);

    //    // Handle wavpac since it has different sources for windows / unix
    //    var wplin = (from item in ret where item.Name == "wavpack-linux" select item).FirstOrDefault();
    //    var wpwin = (from item in ret where item.Name == "wavpack-win" select item).FirstOrDefault();
    //    if (GlobalScript.IsOsUnix())
    //    {
    //        if (wpwin != null) ret.Remove(wpwin);
    //        if (wplin != null) wplin.Name = "wavpack";
    //    }
    //    else
    //    {
    //        if (wplin != null) ret.Remove(wplin);
    //        if (wpwin != null) wpwin.Name = "wavpack";
    //    }
    //    return ret;
    //}

    /// <summary> List of Depend Names / Paths. </summary>
    public static List<SourcePackage> GetDepends()
    {
        var ret = new List<SourcePackage>
            {
                new SourcePackage("sox", "14.4.2","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/sox/sox/{Version}/{Name}-{Version}.tar.gz"),

                new SourcePackage("flac", "1.3.1","{Name}-{Version}.tar.xz","{Name}",
                    "http://downloads.xiph.org/releases/{Name}/{Name}-{Version}.tar.xz"),

                new SourcePackage("libid3tag", "0.15.1b","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/mad/{Name}/{Version}/{Name}-{Version}.tar.gz"),

                new SourcePackage("libmad", "0.15.1b","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/mad/{Name}/{Version}/{Name}-{Version}.tar.gz"),

                new SourcePackage("lame", "3.99.5","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/lame/{Name}/3.99/{Name}-{Version}.tar.gz"),

                new SourcePackage("libogg", "1.3.2","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.xiph.org/releases/ogg/{Name}-{Version}.tar.gz"),

                new SourcePackage("libpng","1.6.17","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/libpng/libpng16/{Version}/{Name}-{Version}.tar.gz"),

                new SourcePackage("libsndfile","1.0.25","{Name}-{Version}.tar.gz","{Name}",
                    "http://www.mega-nerd.com/libsndfile/files/{Name}-{Version}.tar.gz"),

                new SourcePackage("speex","1.2rc2","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.xiph.org/releases/speex/{Name}-{Version}.tar.gz"),

                new SourcePackage("libvorbis","1.3.5","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.xiph.org/releases/vorbis/{Name}-{Version}.tar.gz"),

                new SourcePackage("zlib","1.2.8","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/libpng/zlib/{Version}/{Name}-{Version}.tar.gz"),


                // TODO Not sure of these
                // not included in the pre-built project files, try regenerating using CMake / Look for links to these from above libs

                //TODO should we delete headers in root dir for this one?
                new SourcePackage("opencore-amr","0.1.3","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/opencore-amr/opencore-amr/{Name}-{Version}.tar.gz"),

                new SourcePackage("amrnb","11.0.0.0","{Name}-{Version}.tar.bz2","{Name}",
                    "http://www.penguin.cz/~utx/ftp/amr/{Name}-{Version}.tar.bz2"),

                new SourcePackage("amrwb","11.0.0.0","{Name}-{Version}.tar.bz2","{Name}",
                    "http://www.penguin.cz/~utx/ftp/amr/{Name}-{Version}.tar.bz2"),

                new SourcePackage("libao","1.2.0","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.xiph.org/releases/ao/{Name}-{Version}.tar.gz"),

                new SourcePackage("twolame","0.3.13","{Name}-{Version}.tar.gz","{Name}",
                    "http://downloads.sourceforge.net/project/twolame/{Name}/{Version}/{Name}-{Version}.tar.gz"),

                new SourcePackage("opus","1.1","{Name}-{Version}.tar.gz","{Name}",
                    "https://ftp.mozilla.org/pub/mozilla.org/{Name}/{Name}-{Version}.tar.gz"),

            };

        // Handle wavpac since it has different sources for windows / unix
        if (GlobalScript.IsOsUnix())
        {
            ret.Add(new SourcePackage("wavpack", "4.70.0", "{Name}-{Version}.tar.bz2", "{Name}",
                "http://www.wavpack.com/{Name}-{Version}.tar.bz2"));
        }
        else
        {
            ret.Add(new SourcePackage("wavpack", "4.70.0", "sources.zip", "{Name}",
                "http://www.wavpack.com/sources.zip"));
        }

        return ret;
    }

    #endregion

}
