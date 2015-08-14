"""
Represents the Depend settings
"""

# Always try to import cElementTree since it's faster if it exists
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import platform
from os.path import join, abspath, exists
from scripts.script_logs import ScriptLogs
from scripts.dep_src_base import DepSource

# XML Settings for Download of Depends
class DependSettings(object):

    def __init__(self):
        """Dependency Settings"""
        super().__init__()
        self.log = ScriptLogs.getlogger()

        # Path to the config file
        self.ConfigPath = None
        self.platform = None

        # XML Root Tag
        self.xmlroot = None

        # Directory properties
        self.DepsDirectory = ""
        self.ArchiveDirectory = ""

        # List of Sources
        self.sources = []

    def read_element(self, tag):
        """Read XML Value Element"""
        nextval = next(self.xmlroot.iter(tag), None)
        if nextval == None : raise ValueError('Element not found: ' + tag)
        return nextval.text

    def loadxml(self):
        """Load XML"""
        # Load in the xml
        tree = ET.ElementTree(file=self.ConfigPath)
        self.xmlroot = tree.getroot()
        if self.xmlroot.tag != 'Settings':
            raise ValueError('Root Element is not Settings')

        # Directory Settings
        self.DepsDirectory = self.read_element('DepsDirectory')
        self.DepsDirectory = abspath(self.DepsDirectory)
        self.ArchiveDirectory = self.read_element('ArchiveDirectory')
        self.ArchiveDirectory = join(self.DepsDirectory, self.ArchiveDirectory)

        # Set the Archive directory for downloaded sources
        DepSource.ArchiveDir = self.ArchiveDirectory
        # Set the root Extract directory for extracting sources
        DepSource.RootExtractDir = self.DepsDirectory

        # Load in the list of download sources
        self.sources = DepSource.parsexml(self.xmlroot)
        return

    def getdeps(self):
        """Download and Extract Sources"""
        for source in self.sources:
            self.log.info("")
            self.log.info("#####################################################")

            # Skip anything already extracted
            extractdir = abspath(join(DepSource.RootExtractDir, source.destsubdir))
            if exists(extractdir):
                self.log.warn("Deps Subdir: " + source.destsubdir + " already exists, skipping")
                continue

            extracted = False
            downloaded = source.download()
            if downloaded == False:
                self.log.error("Download Failed")
            else:
                extracted = source.extract()

            # Remove the archive file
            source.remove_archivefile()
        return

    def get_configpath(self):
        log = ScriptLogs.getlogger()
        """Determine which config filename / path to use"""
        self.platform = platform.system()
        settingsfile = ""
        if self.platform == "Windows":
           settingsfile = "DependSettings_win32.xml"
        elif self.platform == "Linux":
            settingsfile = "DependSettings_linux.xml"
        else:
            log.critical("Unsupported platform")
            self.ConfigPath = None
        self.log.info("Platform identified as: " + self.platform)
        self.log.info("Settings file: " + settingsfile)
        self.ConfigPath = abspath(settingsfile)
        return self.ConfigPath
