# LibMad Changes

## Overview

LibMad is the Mp3 decoder used by libsox to read in mp3 files for later processing

## Applied Changes

### Custom CMake File

TODO

LibMad doesn't appear to come with a cmake file by default
so I've created one which is copied across during the patching stage
This includes the output of the generated libs into build\cmake\LibOutput


## TODO Yet to apply changes

### X64 Assembly fix

For LibMad we need to avoid assembly being compiled for x64 (as x64 doesn't support in-line assembly within C)

First within the libMad Project, open up the config.h file
get rid of FPM_INTEL, and replace it with FPM_DEFAULT

  //#define FPM_INTEL
  #define FPM_DEFAULT

Do the same within mad.h

  //#define FPM_INTEL
  #define FPM_DEFAULT
