#load "Archive.cs"
#load "Depend.cs"
#load "DependLibSox.cs"
#r "..\..\deps\SharpZipLib.0.86.0\lib\20\ICSharpCode.SharpZipLib.dll"
#r "..\..\deps\NLog.3.2.1\lib\net45\NLog.dll"
#r "..\..\deps\SevenZipSharp.0.64\lib\SevenZipSharp.dll"

Archive.SevenZipDllPath = "..\..\deps\SevenZipSharp.Interop.9.38\build\net451\"
DependLibSox.Main(Env.ScriptArgs.ToArray());
