# Lame Changes

## Overview

Lame is the mp3 encoder typically used by libsox for generating mp3 file outputs

## Applied Changes

### Custom CMake File

Lame doesn't appear to come with a cmake file by default
so I've created one which is copied across during the patching stage
This includes the output of the generated libs into build\cmake\LibOutput


## TODO Yet to apply changes

### X64 Fix

In order to get lame to build under X64 in the original patch set 
I had to comment out a line within configMS.h

  #ifdef _M_X64
          //#define HAVE_XMMINTRIN_H
  #endif

### Compiler Options

Another change in the original patch set for 3.99.5 was to change one of the compiler options

 * Project Properties -> Configuration Properties -> C/C++ -> Optimization -> Whole Program Optimization -> **No**

