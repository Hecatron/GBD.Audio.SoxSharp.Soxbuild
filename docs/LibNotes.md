# Notes

## ZLib

Zlib is typically needed for compiling libpng
Change include:

 * Change to output path build\cmake\LibOutput

## LibPng

Libpng allows for spectrograms etc as part of libsox, it depends on zlib
Changes include:

  * Change to output path build\cmake\LibOutput
  * Added a setter for ZLIB_ROOT to find the zlib library
  * Added an include directory for the cmake zlib output directory

  set(ZLIB_ROOT "${CMAKE_BINARY_DIR}/../LibOutput/Release" "${CMAKE_CURRENT_SOURCE_DIR}/../zlib")
  include_directories("${CMAKE_BINARY_DIR}/../zlib")

## MP3 / Lame / Mad

TODO

 * http://sourceforge.net/p/sox/code/ci/master/tree/INSTALL

## Usefull links

 * http://www.cmake.org/Wiki/CMake_Useful_Variables
 * MESSAGE( STATUS "TEST CMAKE_CURRENT_BINARY_DIR:         " ${CMAKE_CURRENT_BINARY_DIR} )
 * MESSAGE( STATUS "TEST CMAKE_CURRENT_SOURCE_DIR:         " ${CMAKE_CURRENT_SOURCE_DIR} )

## Libsox

Libsox is the main library we want to compile but we're compiling it as a dll

### General Changes

 * Change to output path build\cmake\LibOutput for gsm library
 * Change to output path build\cmake\LibOutput for lpc10 library
 * Change to output path build\cmake\LibOutput for libsox library
 * Add the output directory to the list of searched directories for libs for libsox via link_directories()
 * swig_wrap.c is copied into the patched source tree during build to export functions to the outside
 * Add swig_wrap.c to the list of format sources so that we can access the dll from the outside via Managed code
 * Change the libsox library type to SHARED to output a dll instead of a static .lib file
 * Add the depend libs gsm.lib lpc10.lib into the libsox library to be linked in via target_link_libraries()
 * soxconfig.h.cmake is copied into the sox/src directory to determine which external libs to enable

### LibPng Support

Changes made to get libsox to use libpng

 * within soxconfig.h.cmake change "#cmakedefine HAVE_PNG 1" to "#define HAVE_PNG 1"
 * target_link_libraries() used to add static libs libpng16.lib zlib.lib
 * spectrogram.c has been added to formats_srcs, it doesn't seem to get added by default
 * Include directories added

include_directories( "${CMAKE_CURRENT_BINARY_DIR}/../../libpng")
include_directories( "${CMAKE_CURRENT_BINARY_DIR}/../../zlib")
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../../libpng")
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../../zlib")


## TODO

Libs left over:

 * amrnb
 * amrwb
 * flac
 * lame - MP3 Encoding
 * libao
 * libid3tag
 * libmad - MP3 Decoding
 * libogg
 * libsndfile
 * libvorbis
 * opencore-amr
 * opus
 * speex
 * twolame
 * wavpack-win
