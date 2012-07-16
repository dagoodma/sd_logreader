# Module SDLogReaderException

class SDLogReaderException(Exception):
    """Base class for exceptions."""

    def __init__(self,message):
        self.message = message

    def str():
        return self.message

    pass

class ConfigException(SDLogReaderException):
    """\
    Raised when config file errors occur.

    Args:
        file (str): config file that was loaded
        message (str):  a message explaining the error
    """
    def __init__(self, message, file=None):
        self.message = message
        self.file = file

    def str(self):
        message = self.message
        if (self.file):
            message += ' in {0}'.format(self.file)
        
        return message

class NotConnectedException(SDLogReaderException):
    """\
    Raised when not connected and should have been. 

    Args:
        message (str): optional explaination message

    """
    def __init__(self,message=None):
        self.message = message

    def str(self):
        message = 'Not connected'
        if (self.message):
            message += ': {0}'.format(self.message)

        return message

class MissingArgumentException(SDLogReaderException):
    """\
    Raised when a required argument was not given, especially when not
    running in interactive mode.

    Args:
        name (str): missing argument's name

    """
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Expected \'{0}\' argument was missing'.format(self.name)

