# Building LibSox as a Dll

## Overview

Since this project is a .Net front end to libsox, we first need to build libsox out as a dll.
This way we can use PInvoke statements from within .Net via swig to make calls to the underlying libsox.dll. <br />
Note this isn't a supported feature of libsox 

.Net Wrapper -> Swig Generated C# code -> LibSox / Swig Wrapper Code

## Downloading the Dependencies

The first step is to download all the required dependencies <br />
There should be a script within the dotCMake directory called DownloadLibSox.bat / DownloadLibSox.sh
which will download all required versions into the deps\archive directory, then extract to the deps\libsoxbuild directory

OpencoreAMR-NB/WB http://sourceforge.net/projects/opencore-amr  Apache
AMR-NB/WB         http://www.penguin.cz/~utx/amr        See library web page
AO                http://xiph.org/ao                    GPL
FLAC              http://flac.sourceforge.net           BSD
LADSPA            http://www.ladspa.org                 LGPL + plugins' licence
Lame MP3 encoder  http://lame.sourceforge.net           LGPL
Twolame MP2 enc.  http://www.twolame.org                LGPL
libltdl           http://www.gnu.org/software/libtool   LGPL
MAD MP3 decoder   http://www.underbit.com/products/mad  GPL
MP3 ID3 tags      http://www.underbit.com/products/mad  GPL
Magic             http://www.darwinsys.com/file         BSD
Ogg Vorbis        http://www.vorbis.com                 BSD
Opus              http://www.opus-codec.org/            BSD
PNG               http://www.libpng.org/pub/png         zlib (BSD-like)
Sndfile           http://www.mega-nerd.com/libsndfile   LGPL
WavPack           http://www.wavpack.com                BSD
