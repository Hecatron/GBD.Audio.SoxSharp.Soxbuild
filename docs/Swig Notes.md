# Swig Notes

## Overview

Swig is an automated tool for parsing C Library's then generating bindings for other languages such as C# / Jave / Ruby etc
In our case we'll be using it to auto generate C# Sources from the libsox library / sox.h 

## Swig Inputs

### Run Script File

The automated swig python script generate_swig.py handles this
for an example of a dos batch file:

```
SET SWIGBIN="C:\1\apps\5\AudioV6\sox.build-14.4.1\swig\swigbin\swig.exe"

SET SWIGINC=%SWIGINC% -I"C:\1\apps\5\AudioV6\sox.build-14.4.1\sox-14.4.1\src"
SET SWIGINC=%SWIGINC% -I"C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include"

%SWIGBIN% %SWIGINC% -namespace BCH.Audio.Sox.swig -csharp sox.i
```

### Swig Input File

Under src\sox-14.4.2\swig-win\swig.i you'll notice an input file for swig

```
%module libsox
 %{
 /* Includes the header in the wrapper code */
 #include "sox.h"
 %}

 /* Add a constructor that can take a IntPtr, and a return of the pointer */
 %typemap(cscode) SWIGTYPE * %{
  public $csclassname(IntPtr cPtr) {
    swigCPtr = new HandleRef(this, cPtr);
  }

  public IntPtr GetswigCPtr()
  {
      return swigCPtr.Handle;
  }

 %}

 /* Add a constructor that can take a IntPtr, and a return of the pointer */
 %typemap(cscode) SWIGTYPE %{
  public $csclassname(IntPtr cPtr) {
    swigCMemOwn = false;
    swigCPtr = new HandleRef(this, cPtr);
  }

  public IntPtr GetswigCPtr()
  {
      return swigCPtr.Handle;
  }

 %}

 /* Parse the header file to generate wrappers */
 %include <windows.i>
 %include "limits.h"
 %include "sox.h"
```

## Swig Outputs

### Running the Script

After running swig against libsox this will generate several files under build\sox_swigcsharp
sox_wrap.c is a file that should be incorperated into the libsox C Source
this way we can access it's functions via the swig wrapper

 * Any files ending in .cs will be C Sharp files we can use as part of the .Net wrapper code
 * Any types should be available as class's such as sox_effect_t
 * In some cases pointers are used, these will show up under swig as types called SWIGTYPE_p_sox_format_handler_t

To convert from a pointer to a class instance, example code: 

```VB
''' <summary>
''' Default Constructor
''' </summary>
Public Sub New(pointer As SWIGTYPE_p_sox_format_handler_t)
    _SwigStorage = New sox_format_handler_t(pointer.GetswigCPtr())
End Sub
```
