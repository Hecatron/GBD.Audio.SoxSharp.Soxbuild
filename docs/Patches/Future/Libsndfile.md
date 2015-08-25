# Libsndfile Changes

## Overview

Libsndfile adds support for certain formats of audio involving AIFF and wav files

## Applied Changes

### Custom CMake File

TODO

Libsndfile doesn't appear to come with a cmake file by default
so I've created one which is copied across during the patching stage
This includes the output of the generated libs into build\cmake\LibOutput

## TODO Yet to apply changes

### Lib Output

The original patch set had an issue with the x64 build outputing to the wrong directory
since we're using our own cmake files this shouldn't be an issue

### File References

The original patch set had problems with the code referencing ogg_*.c files
since we're generating our own cmake file this shouldn't be an issue

