# Notes

## Usefull links

 * http://www.cmake.org/Wiki/CMake_Useful_Variables
 * MESSAGE( STATUS "TEST CMAKE_CURRENT_BINARY_DIR:         " ${CMAKE_CURRENT_BINARY_DIR} )
 * MESSAGE( STATUS "TEST CMAKE_CURRENT_SOURCE_DIR:         " ${CMAKE_CURRENT_SOURCE_DIR} )


## TODO Changes not yet rolled in

### Test X64 Output

First we'll get 32bit support working, then check to see if the cmake x64 Visual Studio generator works in terms of compiling the src

### Disable Warnings as Errors

In the original set of changes I needed to disable "show warnings as Errors" in the VS Project Files (set to No)

  * Project Properties -> Configuration Properties -> C/C++ -> General -> Treat Warnings as Errors

For the following projects

  * LibId3Tag
  * LibMp3Lame
  * LibSpeex
  * LibVorbis
  * LibWavPack
  * LibFlac
  * LibSndFile
  * LibSox

This may already be the case for the output generated via cmake

### MP3 / Lame / Mad

TODO

 * http://sourceforge.net/p/sox/code/ci/master/tree/INSTALL

### List of Libs outstanding

List of libraries I need to look at to see if they can be rolled into the build process

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
