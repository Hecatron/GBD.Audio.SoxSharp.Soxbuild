using System;
using System.IO;

/// <summary> Gobal Script Functions. </summary>
public class GlobalScript
{

    #region "Functions - Static"

    /// <summary> Check if the Operating System is Unix. </summary>
    public static bool IsOsUnix() {
        int p = (int)Environment.OSVersion.Platform;
        if ((p == 4) || (p == 6) || (p == 128)) return true;
        return false;
    }

    /// <summary> Get the current location of the running script. </summary>
    public static string ScriptRunLocation() {
        // TODO find a better way to do this using Assembly.GetAssembly().Location
        string location = Path.Combine(Environment.CurrentDirectory,"scripts");
        return location;
    }

    #endregion

}