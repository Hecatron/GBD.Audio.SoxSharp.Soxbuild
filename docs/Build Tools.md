# Build tools

## Overview

This is a list of build tools required to build the sources

## Build Tools

### Python 3.x

The build scripts are primarily written in Python 3.x

 * https://www.python.org/

### CMake

CMake is used for the generation of Project Files for different platforms for libsox

 * http://www.cmake.org/

### Visual Studio 2013 / MSBuild

Currently the sources are set to build via MSBuild / Visual Studio 2013
I've been debugging the python scripts using VS2015 / Python Tools (there's a solution within the bin/vsdebug directory)
But VS2013 is needed to compile libsox

## Auto Downloaded Tools

### Swig 3.0

As part of the download srcs script, swig 3.0 is auto downloaded for generating C# Code from the C code within libsox

 * http://www.swig.org/download.html
