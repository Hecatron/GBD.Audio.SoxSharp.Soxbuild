#load "Lib\GlobalScript.cs"
#load "Paths.cs"
#load "CMakeGenerate.cs"

#r "..\..\deps\NLog.3.2.1\lib\net45\NLog.dll"

// Set path to Nlog Configuration
string logFilePath = GlobalScript.AbsPath("NLog.config");
NLog.LogManager.Configuration = new NLog.Config.XmlLoggingConfiguration(logFilePath, true);

// Make Call to Main App
CMakeGenerate.Main(Env.ScriptArgs.ToArray());