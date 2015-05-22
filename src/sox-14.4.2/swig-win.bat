SET SWIGBIN="C:\1\apps\5\AudioV6\sox.build-14.4.1\swig\swigbin\swig.exe"
SET SWIGINC=%SWIGINC% -I"C:\1\apps\5\AudioV6\sox.build-14.4.1\sox-14.4.1\src"
SET SWIGINC=%SWIGINC% -I"C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include"
%SWIGBIN% %SWIGINC% -namespace BCH.Audio.Sox.swig -csharp sox.i
