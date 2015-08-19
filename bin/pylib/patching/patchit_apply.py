"""
Wrapper for patchit for applying patches to multiple files
"""

# This module uses patchit from https://pypi.python.org/pypi/patchit/1.1

import os, patchit

# Wrapper class for patching sources
class PatchitApply(object):

    # Class Constructor
    def __init__(self, patchfile, startdir, strip = 0):
        self.patchfile = patchfile
        self.startdir = startdir
        self.strip = strip

    # Apply a Patch file to the given directory
    def Apply(self):
        with open(self.patchfile) as patch_hand:
            patches = patchit.PatchSet.from_stream(patch_hand)

            for patchitem in patches:
                # Figure out the path of the file to patch
                srcpath = PatchitApply.StripPath(patchitem.source_filename, self.strip)
                srcpath = os.path.abspath(os.path.join(self.startdir, srcpath))
                
                with open(srcpath) as srcfile_hand:
                    # Get a read handle to the file to patch
                    srcfile_iter = (x.strip('\n') for x in iter(srcfile_hand.readline, ''))
                    # Read in the file and patch in memory
                    outlist = list(patchitem.merge(srcfile_iter))

                    # Overwrite file
                    with open(srcpath, 'w') as file:
                        for item in outlist:
                            file.write("{}\n".format(item))

                    # TODO test with multiple files / multiple patches
                    # And check the carriage return outputed
        return

    # Strip parts from the front of a relative path
    @staticmethod
    def StripPath(filepath, strip = 0):
        pathparts = filepath.split(os.sep)
        for x in range(0, strip):
            pathparts.pop(0)
        retpath = os.path.join(*pathparts)
        return retpath