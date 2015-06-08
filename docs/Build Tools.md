# Build tools

## Overview

This is a list of build tools and libraries contained within this bin/binfiles directory

## Build Tools

### ScriptCs

http://scriptcs.net/

**Scriptcs** is used for running all build related scripts (in C#).
Actual scripts in C# are stored within the bin/scripts directory

At the moment I couldn't get .csx files to be recognised fully within Visual Studio as code files.
So code such as Main_Depend.csx acts as a jumping off point to a .cs file where the actual code sits.
The bin/scripts/Testing directory contains Visual Studio Solution / Projects for testing and developing the build scripts

### NuGet

* https://www.nuget.org/

We use the **Nuget.exe** for the auto downloading of dependencies for .Net Projects contained within this Project.
This allows us to more easily download .Net depends of specific versions.
The packages.config file witihn the scripts directory is used for a general list of which .Net depends to download
into the /deps/ directory

Use the following command to update itself

  nuget update -self

### CMake

* http://www.cmake.org/

CMake is used for the generation of Project Files for different platforms for libsox

### Swig 3.0

* http://www.swig.org/download.html

Swig is used for the generation of code as part of the wrapper

## .Net Libraries

### NLog

http://nlog-project.org/

NLog is used for console output and general logging, it can be customised by editing the NLog.config <br />
TODO Look into Common Logging

### SharpZipLib

http://icsharpcode.github.io/SharpZipLib/

SharpZipLib is used for the unpacking of non .Net dependencies / extraction of compressed files

### SevenZipSharp

SevenZipSharp is used for handling 7zip files and xz files such as flac.tar.xz

TODO Check this is cross platform compatible