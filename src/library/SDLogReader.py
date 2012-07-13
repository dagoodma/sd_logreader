# Module SDLogReader
import serial
import pprint
import logging
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
        self.greeting = """
Welcome to the sd_logreader tool.
Enter 'help' for a list of commands.
"""

        self.goodbye = """
Goodbye!"""

        self.prompt = '> '
        self.want_exit = False
        self.config = config;
        self.config_file = config_file
        self.connections = dict()
        self.timeout = self.config.getint('DEFAULT', 'timeout')
        self.last_id = 0

        # Read config and connect to serial ports
        logging.debug('Connecting to devices: ' + str(self.config.sections()))
        for device in self.config.sections():
            if (not self.config.has_option(device, 'port')):
                raise MissingPortException(self.config_file, device)
            
            port = self.config.get(device,'port')
            baud = self.config.get('DEFAULT','baud') # default

            logging.debug('Connecting to \'' + device + '\' on port: ' + str(port) + ', with baudrate: ' + str(baud))
            
            if (self.config.has_option(device,'baud')):
                baud = self.config.get(device,'baud')
            
            # Connect to port
            self.connections[device] = 'test'
            """serial.Serial(
                port = port,
                baudrate = baud,
                timeout = self.timeout
                )
            )
            """
            logging.info('Connected to: ' + device)


        logging.debug('Finished connecting to devices')

    """Deconstructor for SDLogReader. Disconnects from all open serial
       ports.
    """
    def __del__(self):
        logging.debug('Disconnecting from devices: ' + str(self.connections.keys()))
        for device in self.connections.iterkeys():
            """
            self.connections(device).close()
            """
            logging.info('Disconnected from: ' + device)

        logging.debug('Disconnected from all devices')


    """Prints a help message listing the available commands.

       Keyword arguments:
       command -- [optional] displays a help message only for the given command
       
    """
    def show_help(self,command=None):
        print """listing \t lists size and id of each log
dumpfile id \t lists size and dumps file with given id
help \t\t shows this help message
exit \t\t exits and disconnects from the devices
"""
        

                
    """Begins a session where the user can interact by typing commands.
       The session is terminated and this function returns when the
       user types the 'exit' command.

       Keyword commands:

    """
    def start(self):
        print(self.greeting)

        while (not self.want_exit):
            user_input = raw_input(self.prompt)
            user_input = user_input.strip().lower()

            # Parse user input
            if (user_input == 'exit'):
                print self.goodbye
                self.want_exit = True
            elif (user_input == 'help'):
                self.show_help()
            elif (user_input == 'listing'):
                print 'Not implemented!'
            elif (user_input == 'dumpfile'):
                print 'Not implemented!'
            else:
                print 'Unknown command: ' + str(user_input) + '\nUse \'help\' for a list of valid commands.'



    """Lists log files from each device as and ID with a size.
    """
    def show_listing():
        # Clear size dictionary to repopulate

        # Iterate through each device
        for
            # Request size of log over serial

            # Add retrieved size to dictionary with associated id


        # Print the 
