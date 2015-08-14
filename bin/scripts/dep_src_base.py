"""
Module for dependency source downloads
"""

import os, glob, shutil, zipfile, tarfile, time
from os.path import join, abspath, exists
from scripts.script_logs import ScriptLogs

# Source Base Class
class DepSource(object):

    ArchiveDir = "."
    RootExtractDir = "."

    def __init__(self):
        self.url = ""
        self.destsubdir = ""
        self.md5hash = ""
        self.version = ""
        self.arch_filename = ""
        self.arch_filepath = ""
        self.subdirmove = 0
        self.log = ScriptLogs.getlogger()

    def download(self):
        return True

    def extract(self):
        if self.arch_filepath == None:
            return False

        # Create the extraction directory
        self.log.info("Extracting: " + self.arch_filename + " To: " + self.destsubdir)
        extractdir = abspath(join(DepSource.RootExtractDir, self.destsubdir))
        if exists(extractdir):
            #shutil.rmtree(extractdir)
            # Skip if destination subdir already exists
            self.log.warn("Skipping: " + self.destsubdir + " Directory already exists")
            return False
        os.makedirs(extractdir)

        # Get the file extension
        extension = os.path.splitext(self.arch_filename)[1]

        # Extract the file
        if extension == ".zip":
            with zipfile.ZipFile(self.arch_filepath, "r") as z:
                z.extractall(extractdir)
        elif extension == ".gz":
            with tarfile.open(self.arch_filepath, 'r:gz') as tfile:
                tfile.extractall(extractdir)
        elif extension == ".xz":
            with tarfile.open(self.arch_filepath, 'r:xz') as tfile:
                tfile.extractall(extractdir)
        elif extension == ".bz2":
            with tarfile.open(self.arch_filepath, 'r:bz2') as tfile:
                tfile.extractall(extractdir)
        else:
            raise ValueError("File Extension: " + extension + " Not supported")

        return True

    # Delete the downloaded archive file
    def remove_archivefile(self):
        if self.arch_filepath == "" or self.arch_filepath == None:
            return False
        elif exists(self.arch_filepath):
            os.remove(self.arch_filepath)
            return True
        else:
            return False

    def movetoparent_multiple(self):
        # Move subdir to parent if required
        for x in range(0, self.subdirmove):
            self.log.info("Moving source directory to parent: " + self.destsubdir)
            # Avoid issues with directory locking
            self.movetoparent()

    # Some sources include a subdirectory with a name / version inside
    # This just moves things around so that all the source sits at the top of the directory within deps
    def movetoparent(self):
        """Move sub directory to parent"""
        parentdir = abspath(join(DepSource.RootExtractDir, self.destsubdir))
        olddir = parentdir + "_old"

        # move the deps/subdir to deps/subdir_old
        if exists(olddir):
            shutil.rmtree(olddir)
        os.rename(parentdir, olddir)
        
        # Relocate the inner directory to /deps/subdir
        innerdir = os.listdir(olddir)[0]
        innerdir = join(olddir, innerdir)
        shutil.move(innerdir, parentdir)
        shutil.rmtree(olddir)
        return

    @staticmethod
    def parsexml(root):
        ret = []

        from scripts.dep_src_http import HttpSource, GitHubZipSource

        for source in root.findall('FileExtract'):
            newsource = FileExtract(
                source.find('SrcFile').text,
                source.find('DestSubDir').text)
            if source.find('Md5Hash') != None:
                newsource.md5hash = source.find('Md5Hash').text
            if source.find('Version') != None:
                newsource.version = source.find('Version').text
            if source.find('SubDirMove') != None:
                newsource.subdirmove = int(source.find('SubDirMove').text)
            ret.append(newsource)

        for source in root.findall('HttpSource'):
            newsource = HttpSource(
                source.find('Url').text,
                source.find('DestSubDir').text)
            if source.find('Md5Hash') != None:
                newsource.md5hash = source.find('Md5Hash').text
            if source.find('Version') != None:
                newsource.version = source.find('Version').text
            if source.find('SubDirMove') != None:
                newsource.subdirmove = int(source.find('SubDirMove').text)
            ret.append(newsource)

        for source in root.findall('GitHubZipSource'):
            newsource = GitHubZipSource(
                source.find('Url').text,
                source.find('DestSubDir').text,
                source.find('CommitId').text)
            if source.find('Md5Hash') != None:
                newsource.md5hash = source.find('Md5Hash').text
            if source.find('Version') != None:
                newsource.version = source.find('Version').text
            if source.find('SubDirMove') != None:
                newsource.subdirmove = int(source.find('SubDirMove').text)
            ret.append(newsource)

        return ret

# File Extract Source for file that has to be manually downloaded into the Archive directory
class FileExtract(DepSource):

    def __init__(self, arcfile, destsubdir):
        super().__init__()
        self.url = arcfile
        self.destsubdir = destsubdir

        #If path is not absolute, assume it's relative to the Archive directory
        if not os.path.isabs(self.url):
            self.url = join(DepSource.ArchiveDir, self.url)
        self.url = abspath(self.url)

        #Assume glob is needed
        globlist = glob.glob(self.url)
        self.arch_filepath = None if not globlist else globlist[0]
        if self.arch_filepath:
            self.arch_filename = os.path.basename(self.arch_filepath)
        return
