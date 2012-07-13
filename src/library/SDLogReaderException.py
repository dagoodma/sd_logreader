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

    Keyword arguments:
        file -- config file that was loaded
        message  -- a message explaining the error
    """

    def __init__(self, file, message):
        self.file = file
        self.message = message

    def str():
        return  self.message + ' in ' + str(self.file)

class NotConnectedException(SDLogReaderException):
    """This exception is raised when an action is attempted when no
       connection has been made.
    """

    def __init__(self):

    def __str__(self):
        return 'Not connected'

