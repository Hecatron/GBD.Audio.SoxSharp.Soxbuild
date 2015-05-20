# Build tools

## Overview

This is a list of build tools and libraries contained within this build/bin directory

## ScriptCs

Ideally I'd like to use scriptcs for 

## CS-Script

We use **cscs.exe** for the running of .cs files as scripts via mono or a .Net runtime environment <br />
This allows us to run .cs files as script instead of requiring to compile them as an exe before hand <br />
CS-Script is released under the MIT Licence and is a managed application

* http://www.csscript.net/

## NuGet

We use the **Nuget.exe** for the auto downloading of dependencies for .Net Projects contained within this Project <br />
This allows us to more easily download .Net depends of specific versions

* https://www.nuget.org/

Use the following command to update itself

  nuget update -self

## SharpZipLib

We use SharpZipLib for the unpacking of non .Net dependencies / extraction of compressed files

* http://icsharpcode.github.io/SharpZipLib/
