"""
Http related sources
"""

import sys, os, wget, hashlib
from os.path import join, exists
from pylib.logwrapper import LogWrapper
from pylib.depend.depsource import DepSource

PY3K = sys.version_info >= (3, 0)
if PY3K:
  import urllib.request as urllib2
  import urllib.parse as urlparse
else:
  import urllib2
  import urlparse

# Http Download Source
class HttpSource(DepSource):

    def __init__(self, httpurl, destsubdir):
        super().__init__()
        self.url = httpurl
        self.destsubdir = destsubdir
        return

    @staticmethod
    def getfilename_fromurl(url):
        """Get Destination filename for a downloaded file"""
        # Try to get destination Filename from Content Disposition
        tmprequest = urllib2.urlopen(url)
        filename = wget.filename_from_headers(tmprequest.info())
        # Get filename from url
        if filename == None:
            filename = wget.filename_from_url(url)
        return filename

    def download(self):
        # Create destination directory if it doesn't exist
        destdir = DepSource.ArchiveDir
        if not exists(destdir):
            os.makedirs(destdir)
        
        # substitute version into the url
        urlversion = self.url.replace("{Version}", self.version)

        # Set paths
        self.arch_filename = HttpSource.getfilename_fromurl(urlversion)
        self.arch_filepath = join(destdir,self.arch_filename)

        # Download file if it doesn't exist
        self.log.info("Downloading :" + self.arch_filename)
        if exists(self.arch_filepath):
            self.log.warn("File already downloaded / Skipping: " + self.arch_filename)
        else:
            wget.download(urlversion, out=destdir)
            print("\n")
            self.log.info("File Downloaded")

        # Check the MD5 Hash
        if self.md5hash:
            self.log.info("Calculating downloaded file hash")
            src_md5sum = hashlib.md5(open(self.arch_filepath,'rb').read()).hexdigest()
            self.log.info("File MD5 Hash is: " + src_md5sum)
            if self.md5hash == src_md5sum:
                self.log.info("MD5 Hash matches Okay: " + self.md5hash)
            else:
                self.log.error("MD5 Hash does not match: " + self.md5hash)
        return True

# GitHub Download Source as zip
class GitHubZipSource(HttpSource):
    
    def __init__(self, giturl, destsubdir, commitid):
        self.commitid = commitid
        self.giturl = giturl

        # commit id can ether be set to "master" for the latest version
        # or a specific commit id for a specific point n time / version
        self.url = giturl + "/archive/" + commitid + ".zip"

        # Base Constructor
        super().__init__(self.url, destsubdir)
        return

    def extract(self):

        # Call base class extraction
        extracted = DepSource.extract(self)
        if extracted == False:
            return False

        # Move subdir to parent
        self.movetoparent()
        return True
