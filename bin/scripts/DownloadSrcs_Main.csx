#load "Lib\GlobalScript.cs"
#load "Lib\Archive.cs"
#load "Lib\SourcePackage.cs"
#load "DownloadSrcs.cs"

#r "..\..\deps\SharpZipLib.0.86.0\lib\20\ICSharpCode.SharpZipLib.dll"
#r "..\..\deps\NLog.3.2.1\lib\net45\NLog.dll"
#r "..\..\deps\SevenZipSharp.0.64\lib\SevenZipSharp.dll"

// Paths should be relative to the script location

// Set path to Nlog Configuration
string logFilePath = Path.Combine(GlobalScript.ScriptRunLocation(), @"NLog.config");
NLog.LogManager.Configuration = new NLog.Config.XmlLoggingConfiguration(logFilePath, true);

// Set path to the 7Zip dll
Archive.SevenZipDllPath = Path.Combine(GlobalScript.ScriptRunLocation(), @"..\..\deps\SevenZipSharp.Interop.9.38\build\net451\");

// Make Call to Main App
DownloadSrcs.Main(Env.ScriptArgs.ToArray());
