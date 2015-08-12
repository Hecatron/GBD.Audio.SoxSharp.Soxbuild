using System;
using System.Diagnostics;
using System.IO;
using NLog;

/// <summary> Gobal Script Functions. </summary>
public class GlobalScript
{

    /// <summary> Used for the Logging Output. </summary>
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    #region "Functions - Static"

    /// <summary> Check if the Operating System is Unix. </summary>
    public static bool IsOsUnix() {
        int p = (int)Environment.OSVersion.Platform;
        if ((p == 4) || (p == 6) || (p == 128)) return true;
        return false;
    }

    /// <summary> Get the current location of the running script. </summary>
    public static string ScriptRunLocation() {
        //string location = AppDomain.CurrentDomain.BaseDirectory;
        //if (Debugger.IsAttached) location = Path.Combine(location, @"..\..\..\..\");
        
        // TODO find a better way to do this using Assembly.GetAssembly().Location
        string location = Path.Combine(Environment.CurrentDirectory,"scripts");
        location = Path.GetFullPath(location);
        return location;
    }

    /// <summary> Calculate Absolute Path in relation to the script. </summary>
    public static string AbsPath(string input) {
        string ret = Path.Combine(ScriptRunLocation(), input);
        ret = Path.GetFullPath(ret);
        return ret;
    }

    #endregion

}
