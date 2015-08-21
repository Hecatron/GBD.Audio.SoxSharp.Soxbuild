cmake_minimum_required(VERSION 2.4)

# Improvised cmake file for Lame MP3 Encoder
# Copied from sox src msvc10 / LibMp3Lame.vcxproj

# TODO the main thing stopping the build is the missing defines
# Although we also need to compare the other VS Project options and look at the wiki to check which Debug type is needed

# 1. Defines

#Additional Defines set:
#
#_WINDOWS
#CMAKE_INTDIR="Debug"
#LibMp3Lame_EXPORTS
#
#Missing the following defines:
#
#_LIB
#_CRT_NONSTDC_NO_WARNINGS
#_CRT_SECURE_NO_WARNINGS
#HAVE_CONFIG_H

# 2. Configuration Properties -> General -> Character Set = Use Unicode Character Set
# 3. Configuration Properties -> C/C++ -> Optimisation -> Inline Function Expansion = Default

# 4. Configuration Properties -> C/C++ -> Code Generation
# Enable String Pooling = Yes
# Enable Minimal Rebuild = Yes
# Runtime Library = Multi Threaded Debug /MTd
# Enable Function Level Linking = Yes
# Floating Point Model = Fast

# TODO Look through linker options if the above don't work


project(lame C)
set(VERSION "3.99.5")

include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/..")
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../include")
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../mpglib")
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/../libmp3lame")

set(LAME_HDRS
    bitstream.h
    ../mpglib/common.h
    config.h
    ../configMS.h
    ../mpglib/dct64_i386.h
    ../mpglib/decode_i386.h
    encoder.h
    fft.h
    gain_analysis.h
    ../mpglib/huffman.h
    id3tag.h
    ../mpglib/interface.h
    ../mpglib/l2tables.h
    l3side.h
    ../include/lame.def
    ../include/lame.h
    lame_global_flags.h
    lame-analysis.h
    lameerror.h
    ../mpglib/layer1.h
    ../mpglib/layer2.h
    ../mpglib/layer3.h
    machine.h
    ../mpglib/mpg123.h
    ../mpglib/mpglib.h
    newmdct.h
    psymodel.h
    quantize.h
    quantize_pvt.h
    reservoir.h
    set_get.h
    ../mpglib/tabinit.h
    tables.h
    util.h
    vbrquantize.h
    VbrTag.h
    version.h
)

set(LAME_SRCS
    bitstream.c
    ../mpglib/common.c
    ../mpglib/dct64_i386.c
    ../mpglib/decode_i386.c
    encoder.c
    fft.c
    gain_analysis.c
    id3tag.c
    ../mpglib/interface.c
    lame.c
    ../mpglib/layer1.c
    ../mpglib/layer2.c
    ../mpglib/layer3.c
    mpglib_interface.c
    newmdct.c
    presets.c
    psymodel.c
    quantize.c
    quantize_pvt.c
    reservoir.c
    set_get.c
    ../mpglib/tabinit.c
    tables.c
    takehiro.c
    util.c
    vbrquantize.c
    VbrTag.c
    version.c
)

add_library(LibMp3Lame SHARED ${LAME_SRCS} ${LAME_HDRS})

# Set the Output Directory for libs
set_target_properties(LibMp3Lame
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../cmake/LibOutput"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../cmake/LibOutput"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../cmake/LibOutput"
)
