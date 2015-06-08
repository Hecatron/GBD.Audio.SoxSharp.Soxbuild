# Building LibSox as a Dll

## Overview

This is part of a larger project to front end libsox with a .Net wrapper.
The aim of this is to build libsox out as a dll with functions exposed via swig.
This way we can use PInvoke statements from within .Net via swig to make calls to the underlying libsox.dll.

.Net Wrapper -> Swig Generated C# code -> LibSox.dll / Swig Wrapper Code

  * Note this isn't a supported feature of libsox
  * TODO Not yet tested under Linux / still under active development

## Build Steps

### Download .Net Dependencies

The first step is to download any .Net dependencies required as part of the build process.
I've already included the depends for this stage in the repo.
But there should be a script setup to download them via Nuget under the bin/ directory

  DownloadDeps.bat
  DownloadDeps.sh

This will download any .Net depends into the deps/ directory.

### Download Sources

The next step is to download all required source code associated with libsox.
Again there's a script setup for this under bin/

  DownloadSrcs.bat
  DownloadSrcs.sh

This will download any source archives into build/archive/ and extract the sources into build/libsoxbuild

### Generating the Swig Code

The next step is to run swig against the libsox sources, this should generate 2 parts of the code

 * The first is the C# code we need to include into the library
 * The second is a header to be included into the libsox build to expose the C functions to the outside

  SwigGenerate.bat
  SwigGenerate.sh
