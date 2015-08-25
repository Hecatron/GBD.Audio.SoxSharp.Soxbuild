# ZLib Changes

## Overview

ZLib appears to be a compression library used by libpng if we decide to roll in support for libpng to libsox

## Applied Changes

### Change to Output Directory

Within the CMakeLists.txt file, we've altered the output directory for the lib to build\cmake\LibOutput

  # Set the Output Directory for libs
  set_target_properties(zlib zlibstatic
      PROPERTIES
      ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
      LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
      RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
  )
