#!/usr/bin/python

import sys
import os
sys.path.append('library/')
import SDLogReader
import string
import pprint
import argparse
import ConfigParser
# import textwrap
# import tree # RB Tree
import logging


"""-------------------------------------------------------------
                              Start
   -------------------------------------------------------------"""

# ----------------------------------
# Initialize some variables
args_raw = string.join(sys.argv)
args_obj = None
pp = pprint.PrettyPrinter(indent=4)
config_filename = '.config.cfg'

# ----------------------------------
# Parse arguments

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
 Connects to Animus GPS devices and lists or retrieves logged data
 from their associated SD card.''',
    usage='sd_logreader.py -h | [--log=LEVEL] [-c config_file] ',
    add_help=False
    )

parser.add_argument('-c','--config', dest='config_file', nargs=1, type=argparse.FileType('r'),
    help='configuration file that specifies serial ports and baud rates for connecting')
parser.add_argument('-h', '--help', action='store_true', dest='want_help',
    help='show this help message and exit')
parser.add_argument('--log', dest='loglevel', action='store', default='INFO',
    help='sets the logging level for messages', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
# parser.add_argument('-m','--help','--more', action='store_true',
#    dest='more', help='prints a help message about infile.')

# Actually parse the arguments given
try:
    #logging.debug('Parsing arguments: ' + args_raw)
    args_obj = parser.parse_args()
    #pp.pprint(args_obj)
    # Config given? Then ensure file is valid
    if (args_obj.want_help):
        parser.print_help()
        sys.exit()
    if (args_obj.config_file):
        config_filename = args_obj.config_file
except Exception, ex:
    print "Exception occured: " + str(ex)
#except ValueOf, ex:
    # logging.exception('Failed parsing arguments')
#    die("Exception occured: " + ex)

# logging.debug('Parsed arguments') # (' + str(len(args_dict)) + ')')


# -------------------------------
# Read config file

config_obj = ConfigParser.ConfigParser()
config_obj.readfp(open(config_filename))
logFileName = config_obj.get('DEFAULT', 'logfile')
#print (logFileName)


# --------------------------------
# Initialize logger
loglevel = getattr(logging, str(args_obj.loglevel).upper())
logging.basicConfig(filename=logFileName,level=loglevel)
logging.info('Started')

#pp.pprint(config_obj.sections())

# --------------------------------
# Create and initialize SDLogReader object
try:
    logging.debug('Initializing SDLogReader')
    mySDReader = SDLogReader.SDLogReader(
        config = config_obj,
        config_file = config_filename)

# --------------------------------
# Start the SDLogReader
    logging.debug('Starting SDLogReader')
    mySDReader.start()
except Exception, ex:
    logging.exception('SDLogReader failed:' + str(ex))
    # print 'Fatal exception: ' + str(ex)
    raise



logging.info('Exiting')
