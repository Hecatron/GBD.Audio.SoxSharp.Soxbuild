# Building LibSox as a Dll

## Overview

This is part of a larger project to front end libsox with a .Net wrapper.
The aim of this is to build libsox out as a dll with functions exposed via swig.
This way we can use PInvoke statements from within .Net via swig to make calls to the underlying libsox.dll.

.Net Wrapper -> Swig Generated C# code -> LibSox.dll / Swig Wrapper Code

  * Note this isn't a supported feature of libsox
  * TODO Not yet tested under Linux / still under active development

This new build process will use cmake to generate the project files for each library before compilation <br />
At the moment we only have cmake files for libsox, not the other libraries, so I'll need to create some

## Build Steps

### Download Srcs

The first step is to download all the sources and exes for swig and libsox, along with all the src
for the libs that libsox depends on

  cd bin
  download_srcss.py

This will download all the sources needed and swig into **build\packages**
the directory build\Archive is just a temporary directory used when downloading and extracting the source archive files

### Generate Swig C# Files

The next step is to generate the C# Files from the sox source

  generate_swig.py

This will generate a bunch of .cs files we can use later on for the .Net wrapper library within build\sox_swigcsharp
and a swig_wrap.c file that we need to include / compile into libsox for the wrapper to work

### Build Sources

The next step is to patch the sources / run cmake on them / then build them

  buil_srcs.py

In some cases some of the sources need to be built before cmake can be run on others
So we do all of this as part of a single script, although each package is broken out into an individual python module
under pylib/srcs_build

cmake will generate some solution and project files under build\cmake we can use to build the library and depends.
Note for libsox Visual Studio 2015 doesn't currently work as a cmake generator target, this has to do with
internal changes to the iobuf / FILE structures that libsox relies on

 * http://stackoverflow.com/questions/31150635/build-error-in-visual-studio-in-perlio-h-and-iobuf

### TODO Files

  * This only generates project files for libsox so far, we need to look at other projects next
  * Linux support
  * configure soxconfig.h.cmake in the sox cmake directory and set it to use external libs
