%module libsox
 %{
 /* Includes the header in the wrapper code */
 #include "../sox-14.4.1/src/sox.h"
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
