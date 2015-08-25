# Flac Changes

## Overview

Flac stands for the "Free Lossless Audio Codec", it'a an additional codec for audio support within libsox

## Applied Changes

### Custom CMake File

TODO

Flac doesn't appear to come with a cmake file by default
so I've created one which is copied across during the patching stage
This includes the output of the generated libs into build\cmake\LibOutput


## TODO Yet to apply changes

### X64 Fix

within bitreader.c, look for a function call called local_swap32_block_
we need to modify this and add in a function called bswap32


```C++

FLAC__uint32 bswap32(FLAC__uint32 x)
{
	return  ((x << 24) & 0xff000000 ) |
			((x <<  8) & 0x00ff0000 ) |
			((x >>  8) & 0x0000ff00 ) |
			((x >> 24) & 0x000000ff );
}
static void local_swap32_block_(FLAC__uint32 *start, FLAC__uint32 len)
{

#ifdef _M_X64
	while (!len) {
		// read value from the array
		FLAC__uint32 tmpval; 
		tmpval = start[len-1];
		
		// bswap the values, onverting little-endian values to big-endian format
		tmpval = bswap32(tmpval);

		// store the value into the array
		start[len-1] = tmpval;
		
		len--;
	}
#else
	__asm {
		mov edx, start
		mov ecx, len
		test ecx, ecx
loop1:
		jz done1
		mov eax, [edx]
		bswap eax
		mov [edx], eax
		add edx, 4
		dec ecx
		jmp short loop1
done1:
	}
#endif

}

```
