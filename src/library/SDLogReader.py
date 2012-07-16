# Module SDLogReader
import serial
import pprint
import logging
from SDLogReaderException import *
from serial.tools.list_ports import *
    
class SDLogReader:
    """\
    SDLogReader connects to the specified serial port. If none is
    given then the user is prompted for one.

    Args:
        baud_rate: number for serial connection's baud rate
        device_port: path or id of the serial device's port
        timeout: number for the serial connection's timeout in seconds
    Returns: 
        an SDLogReader object
    Raises:
        
       
    """
    def __init__(self, baud_rate, device_port, timeout, interactive=True):
        self.greeting = "\nWelcome to the sd_logreader tool."

        self.goodbye = "\nGoodbye!"

        self.prompt = '> '
        self.want_exit = False
        self.is_connected = False
        self.connection = None
        self.baud_rate = baud_rate
        self.device_port = device_port
        self.interactive = interactive
        self.last_id = 0
        try:
            self.timeout = int(timeout)
        except ValueError, TypeError:
            self.timeout = 5
    

        # Ensure port and baud rate are supplied if we can't query 
        if not self.interactive:
            if not self.device_port:
                raise MissingArgumentException('device')
            if not self.baud_rate:
                raise MissingArgumentException('baud')
        else:
            self.ask_connect()


        self.connect()


    
    def ask_connect(self):
        """\
        Lists available serial devices and queries the user for a
        valid serial device and baud rate. Loops until valid parameters
        are supplied.

        """

        print(self.greeting)

        # Query the user for a serial port
        self.validate_port() # clears the port if it does not exist
        if not self.device_port:
            self.list_ports()
            while not self.device_port:
                self.device_port = self.ask_port()
                self.validate_port()

        # Query the user for a baud rate
        self.validate_baud()
        while not self.baud_rate:
            self.baud_rate = self.ask_baud()
            self.validate_baud()



    def connect(self):
        """\
        Connects to a serial device.

        """
        logging.debug('Connecting to \'{0}\' at {1!s} baud'.format(self.device_port, self.baud_rate))
        try:
            self.connection = serial.Serial(port = self.device_port, baudrate = self.baud_rate, timeout=self.timeout)
        except (ValueError, SerialException) as ex:
            message = 'Failed to connect to \'{0}\': {1!s}'.format(self.device_port, ex)
            logging.exception(message)
            if self.interactive:
                print(message)
            raise
            # TODO try again or prompt for a new port
        self.is_connected = True
        message = 'Connected to \'{0}\''.format(self.device_port)
        logging.info(message)
        if self.interactive:
            print('{0}.\n'.format(message))



    def __del__(self):
        """\
        Deconstructor for SDLogReader.

        """
        self.disconnect()

    def validate_baud(self):
        """\
        Ensure that baud_rate is an integer or clear it.

        """
        logging.debug('Validating baud_rate \'{0!s}\''.format(self.baud_rate))
        try:
            self.baud_rate = int(self.baud_rate)
        except ValueError, TypeError:
            print('Invalid baud rate \'{0!s}\''.format(self.baud_rate))
            self.baud_rate = None

    def validate_port(self):
        """\
        Ensure that device_port exists or clear it.

        """
        logging.debug('Validating port \'{0}\''.format(self.device_port))
        if self.device_port and not os.path.exists(self.device_port):
            print('No such device \'{0}\''.format(self.device_port))
            self.device_port = None

    def disconnect(self):
        """\
        Disconnects from an open serial port.

        """
        # Are we connected?
        if (self.is_connected and self.connection):
            logging.debug('Disconnecting from device \'{0}\''.format(self.device_port))
            self.connection.close()
            logging.info('Disconnected from device \'{0}\''.format(self.device_port))

    def show_help(self,command=None):
        """\
        Prints a help message listing the available commands.

        Args:
            command: [opt] show help for the command


        """
        print """\
listing \t lists size and id of each log
dumpfile id \t lists size and dumps file with given id
info \t\t shows information about the serial connection
help \t\t shows this help message
exit \t\t exits and disconnects from the devices
"""
        
                
    def start_terminal(self):
       """\
        Begins a session where the user can interact by typing commands.
        The session is terminated and this function returns when the user
        types the 'exit' command.

        """
        #pp = pprint.PrettyPrinter(indent=4)

        print('Enter a command. For a list type \'help\'.')

        # Main loop
        while (not self.want_exit):
            user_input = raw_input(self.prompt)

            self.execute_command(user_input)


    
    def execute_command(self,command):
        """\
        Parses and executes the given command. Valid commands are
        documented in the show_help() function.

        Args:
            command: string to be parses and executed
        Returns:
            error or success code
            0 -- success 
            * -- error code

        """
        # Parse command
        command = command.strip().lower()

        # Execute command
        if (command == 'exit'):
            print self.goodbye
            self.want_exit = True
        elif (command == 'help'):
            self.show_help()
        elif (command == 'listing'):
            print('Not implemented!')
        elif (command == 'dumpfile'):
            print('Not implemented!')
        elif (command == 'info'):
            print('Connected to \'{0}\' at {1!s} baud.'.format(self.device_port,self.baud_rate))
        else:
            print('Unknown command \'{0}\'\nUse \'help\' for a list of valid commands.'.format(command))


    
    def ask_port(self):
       """\
        Queries the user to enter a serial device port.

        Returns:
            the device port path or id given by the user.

        """
        user_input = raw_input('Choose a port: ')
        return user_input.strip()


    def ask_baud(self):
        """\
        Queries the user for a baud rate.

        Returns:
            the baud rate given by the user.

        """
        default_str = ''
        if (self.baud_rate):
            default_str = ' [%s]' % self.baud_rate
        user_input = raw_input('Choose a baud rate%s: ' % default_str)
        return user_input.strip()

    def list_ports(self):
        """\
        Lists the available serial ports.

        """
        # Build a port list
        port_list_all = comports()
        port_list = list()
        for device in port_list_all:
            port_list.append(device[0])

        print('Available serial ports:')
        for port in port_list:
            print('\t{0}'.format(port))


    def show_listing(self):
        """\
        Lists log files from the connected device with an ID and a size.

        """
        # Ensure a connection was made

        # Request log file sizes over serial
        logging.debug('Retrieving log file sizes (' + str(count) + ')')

        # Parse response into a list to show the user


    def dump_file(id):
        """\
        Requests the file with the given ID from the connected device.

        """
        # Ensure a connection was made

        # Ensure file with the given id exists
        logging.debug('Retrieving log file ' + str(id) + ' (' + str(size) + ')')
        

        # Request file over serial

        logging.info('Recieved log file ' + str(id))

        # Dump to terminal (for now)
