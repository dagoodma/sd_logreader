# Module SDLogReader
import serial
import pprint
import logging
from SDLogReaderException import *
from serial.tools.list_ports import *
    
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
"""

        self.goodbye = """
Goodbye!"""

        self.prompt = '> '
        self.want_exit = False
        self.config = config;
        self.config_file = config_file
        self.is_connected = False
        self.connection = None
        self.connection_port = None
        self.connection_baud = self.config.get('DEFAULT','baud')
        self.connection_timeout = self.config.getint('DEFAULT', 'timeout')
        self.last_id = 0

    """Deconstructor for SDLogReader. Disconnects from all open serial
       ports.
    """
    def __del__(self):
        # Are we connected?
        if (self.is_connected and self.connection):
            logging.debug('Disconnecting from device: ' + self.connection_port)
            self.connection.close()
            logging.info('Disconnected from device: ' + self.connection_port)


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
        pp = pprint.PrettyPrinter(indent=4)

        # Build a port list
        port_list_all = comports()
        port_list = list()
        for device in port_list_all:
            port_list.append(device[0])

        # Determine serial port to connect to
        print('Available serial ports:')
        self.show_ports(port_list)
        user_input = raw_input('Choose a port: ')
        self.connection_port = user_input.strip()
        user_input = raw_input('Choose a baudrate [' + str(self.connection_baud) + ']: ')
        if (user_input):
            self.connection_baud = int(user_input.strip())

        # Connect to the given port
        logging.debug('Connecting to \'' + self.connection_port + '\' with baudrate: ' + str(self.connection_baud))
        self.connection = serial.Serial(port = self.connection_port, baudrate = self.connection_baud, timeout=self.connection_timeout)
        self.is_connected = True
        logging.info('Connected to: ' + self.connection_port)
        print('Successfully connected to \'' + self.connection_port + '\'.\n')

        #TODO Error handling for connections and a retry loop

        print('Enter a command. For a list type \'help\'.')

        # Main loop
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

    """Lists the available serial ports.
    """
    def show_ports(self, port_list):

        for port in port_list:
            print('\t' + port)


    """Lists log files from the connected device with an ID and a size.
    """
    def show_listing():
        # Ensure a connection was made

        # Request log file sizes over serial

        # Parse response into a list to show the user


    """Requests the file with the given ID from the connected device.
    """
    def dump_file(id):
        # Ensure a connection was made

        # Ensure file with the given id exists
        logging.debug('Retrieving log file ' + str(id) + ' (' + str(size) + ')')
        

        # Request file over serial

        logging.info('Recieved log file ' + str(id))

        # Dump to terminal (for now)
