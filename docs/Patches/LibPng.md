# LibPng Changes

## Overview

Libpng allows for spectrograms etc as part of libsox, it depends on zlib

## Applied Changes

### Change to Output Directory

Within the CMakeLists.txt file, we've altered the output directory for the libs to build\cmake\LibOutput

  set_target_properties( ${PNG_LIB_NAME} ${PNG_LIB_NAME}_static
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../LibOutput"
  )

### Set ZLib Source

Since libpng depends on zlib, and we've put the sources in an unusual place
we need to tell libpng where to find zlib, and include it's sources

ZLIB_ROOT tells cmake where to find the zlib sources, and include_directories adds the zlib directory to the include path

  set(ZLIB_ROOT "${CMAKE_BINARY_DIR}/../LibOutput/Release" "${CMAKE_CURRENT_SOURCE_DIR}/../zlib")
  include_directories("${CMAKE_BINARY_DIR}/../zlib")


## Changes to Libsox

### SoxConfig.h.cmake

Within the soxconfig.h.cmake file we need to enable png by changing
"#cmakedefine HAVE_PNG 1" to "#define HAVE_PNG 1"

also spectrogram.c has been added to formats_srcs, it doesn't seem to get added by default

### Include Directories

In order to add support to libsox we need to add the include directories for zlib and libpng
to the libsox CMakeLists.txt file

  include_directories( "${CMAKE_CURRENT_BINARY_DIR}/../../libpng")
  include_directories( "${CMAKE_CURRENT_BINARY_DIR}/../../zlib")
  include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../../libpng")
  include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../../zlib")

### Target Libs

We also need to use target_link_libraries to get the linker to link in the libs for libpng / zlib into libsox

  target_link_libraries(lib${PROJECT_NAME} libpng16.lib zlib.lib)
