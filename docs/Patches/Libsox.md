# Libsox Changes

## Overview

Libsox is the main library we want to compile but we're compiling it as a dll which is a non standard method for building libsox

## Applied Changes

### Change to Output Directory

Within the CMakeLists.txt file, we've altered the output directory for the libs and dll' to build\cmake\LibOutput
This has been done for gsm, lpc10, libsox

  # Set the Output Directory for libs
  set_target_properties( gsm
      PROPERTIES
      ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
      LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
      RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
  )

### Link Directories

One of the changes made within the libsox CMakeLists.txt file is to add the LibOutput directory to the list of directories
to search for libs to link into the project, this way we can link in gsm.lib, lpc10.lib and any other libs into the main libsox.dll

  # Add the LibOutput directory into the linker path for picking up other libs
  link_directories(${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput)

### Addition of swig sources

In order to access the libsox .dll via swig's generated wrapper code we need to incorperate swig_wrap.c into the libsox project
This includes copying swig_wrap.c into the patched/sox/src directory and modifying the CMakeLists.txt file

  set(formats_srcs
    spectrogram.c
    swig_wrap.c

This should allow us access to the swig functions when loading the libsox.dll
also I've added spectrogram.c into the list of sources since it seems to be missing by default for some reason
(used when rolling in the libpng / zlib libs)

### Change of libsox lib to shared

Because we want the libsox library to be outputed as a dll we need to change the lib output type to shared

  add_library(lib${PROJECT_NAME} SHARED

Because of this change we also need to manually link in the libs for gsm / lpc10 via target_link_libraries

  # Add the depend libs into the linker
  target_link_libraries(lib${PROJECT_NAME} gsm.lib lpc10.lib)

### SoxConfig CMake File

In order to turn different options on and off to include external libs into libsox
we copy across a file called soxconfig.h.cmake into the patched/sox/src directory
This can be tinkered with to enable support for additional libraries


## TODO Yet to apply changes

### BitRate Patch

when converting audio to 8Khz for vox I ran up against certain errors during runtime
so I had to disable the following line

within effects_i_dsp.c on line 135 in function update_fft_cache comment out the line (add 2 slashes)

  //assert(fft_len >= 0);

assert has no functional value, it just checks to see if a condition is true and then errors out the app deliberately if it isn't as a check 

### Library Path Fix

One of the things we need to fix is where libsox looks for it's other dll's when loading for x32 or x64
This way we can have both set's of dll's on a machine for websites

Within **win32-ltdl.c** (Shared Sources)
Within the **LoadLib** function 

Change "const char* szPaths[2];" to "const char* szPaths[5];"

Also add the following just above the for loop 

```C++

#ifdef _M_X64
	szPaths[cPaths++] = "sox-14.4.1-x64/";
	szPaths[cPaths++] = "C:\\WINDOWS\\system32\\sox-14.4.1\\";
#else
	szPaths[cPaths++] = "sox-14.4.1-x32/";
	szPaths[cPaths++] = "C:\\WINDOWS\\SysWOW64\\sox-14.4.1\\";
	szPaths[cPaths++] = "C:\\WINDOWS\\system32\\sox-14.4.1\\";
#endif

```

### Disable Wavpack

Situation may be different for this one because of cmake:

For some reason there seems to be linking errors when we use wavpack with libsox, probably another x64 issue
within soxconfig.h (Config Headers), disable wavpack

```C++
/*
#define HAVE_WAVPACK 1

#define HAVE_WAVPACK_H 1

#define STATIC_WAVPACK 1
*/
```

### LibSox useage memory leak

This one may be out of date with the newer sources
This was discovered with http://vld.codeplex.com/

When we do a search for an effect handler or find effect, typically we end up with a memory leak associated with the useage string

**effects_i.c**

```C++
char * lsx_usage_lines(char * * usage, char const * const * lines, size_t n)
{
  if (!*usage) {
    size_t i, len;
    for (len = i = 0; i < n; len += strlen(lines[i++]) + 1);
    //*usage = lsx_malloc(len); /* FIXME: this memory will never be freed */
    //strcpy(*usage, lines[0]);
    //for (i = 1; i < n; ++i) {
    //  strcat(*usage, "\n");
    //  strcat(*usage, lines[i]);
    //}
  }
  return *usage;
}
```

### LibSox Effect memory leak

This one may be out of date with the newer sources
A problem with freeing up memory on the effect's private storage area 

**effects.c**

```C++
void sox_delete_effect(sox_effect_t *effp)
{
  uint64_t clips;
  unsigned f;

  if ((clips = sox_stop_effect(effp)) != 0)
    lsx_warn("%s clipped %" PRIu64 " samples; decrease volume?",
        effp->handler.name, clips);
  if (effp->obeg != effp->oend)
    lsx_debug("output buffer still held %" PRIuPTR " samples; dropped.",
        (effp->oend - effp->obeg)/effp->out_signal.channels);
      /* May or may not indicate a problem; it is normal if the user aborted
         processing, or if an effect like "trim" stopped early. */
  effp->handler.kill(effp); /* N.B. only one kill; not one per flow */
  if (effp->flows > 0) {
	  for (f = 0; f < effp->flows ; ++f) free(effp[f].priv);
  }
  else {
	  free(effp->priv);; /* Close if single effect */
  }
  free(effp->obuf);
  free(effp);
}
```

### Additional Depends

In the original patch set we added the following for lib depends / target linking

  $(OutDir)LibFlac.lib
  $(OutDir)LibGsm.lib
  $(OutDir)LibId3Tag.lib
  $(OutDir)LibLpc10.lib
  $(OutDir)LibOgg.lib
  $(OutDir)LibPng.lib
  $(OutDir)LibSndFileG72x.lib
  $(OutDir)LibSndFileGSM610.lib
  $(OutDir)LibSpeex.lib
  $(OutDir)LibVorbis.lib
  $(OutDir)LibZLib.lib
  $(OutDir)LibMp3Lame.lib
  $(OutDir)LibMad.lib
  $(OutDir)LibSndFile-1.lib
  winmm.lib

### Unmanaged memory leaks

One of the problems I had with the original non cmake / older libsox version
was unmanaged memory leaks so I need to check this with this version
