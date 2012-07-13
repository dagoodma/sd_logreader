# Module SDLogReader
from SDLogReaderException import *

class SDLogReader:
    """SDLogReader connects to all servers specified the given
       ConfigParser object. Each section represents a different
       server with a unique serial port and an optional baud rate.

       Keyword arguments:
       config -- initialized ConfigParser object
       config_file -- config filename for error reporting

    """

    def __init__(self,config,config_file):
        """Constructor for SDLogReader object"""
        self.config = config;
        self.config_file = config_file
        for section in self.config.sections():
            if (not self.config.has_option(section, 'port')):
                raise MissingPortException(self.config_file, section)
        
                

