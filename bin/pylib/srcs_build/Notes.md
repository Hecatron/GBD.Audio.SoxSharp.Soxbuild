# Notes

## Patch Generation

To generate patches, use:

  diff -Naur [src[] [dest]

diff and patch are gnu tools, included with cgywin or kdiff3

## CMake Notes

### Useful Variables

 * http://www.cmake.org/Wiki/CMake_Useful_Variables

### Build Output Directory

When setting the output directory for a given project, it's best to modify CMakeLists.txt
and do this at the cmake level instead of via msbuild

 * https://cognitivewaves.wordpress.com/cmake-and-visual-studio/
 * http://stackoverflow.com/questions/6594796/how-do-i-make-cmake-output-into-a-bin-dir

An example of setting an output directory for a target within cmake

  set_target_properties( gsm
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
  )

### Lib / Link Search Path

When one build needs to find libraries from another build it's best to set this at the cmake level
AdditionalLibPaths doesn't seem to get passed to the linker within msbuild for some reason

env variables can be set as a work around
But it's better to do this within CMakeLists.txt via a patch instead

 * http://stackoverflow.com/questions/15654002/adding-additional-library-and-include-paths-when-compiling-from-command-line

This way we can also build the project from within Visual Studio

Cmake Example:

  link_directories(${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput)

### MSBuild Verbose Output

For additional output from msbuild try the option:

  /v:diagnostic
