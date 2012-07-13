# Module SDLogReaderException

class SDLogReaderException(Exception):
    """Base class for exceptions."""

    def __init__(self,message):
        self.message = message

    def str():
        return self.message

    pass

class ConfigException(SDLogReaderException):
    """This exception is raised when something is wrong with the
       config file.

    Attributes:
        file -- config file that was loaded
        message  -- a message explaining the error
    """

    def __init__(self, file, message):
        self.file = file
        self.message = message

    def str():
        return  self.message + ' in ' + str(self.file)

class MissingPortException(ConfigException):
    """This exception is raised when a server/section is missing
       a 'port' option.

       Attributes:
           file -- config file loaded
           section -- section/server name that was missing a port option
    """

    def __init__(self, file, section):
        self.file = file
        self.section = section

    def __str__(self):
        return 'section \'' + self.section + '\' missing port option in ' + str(self.file)

