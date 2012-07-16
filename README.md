## SDLogReader for ANIMA ##

*   Website: http://byron.soe.ucsc.edu/ANIMA/SDLogReader
*   Source: https://github.com/mavlink/mavlink
*   Mailing list: [Google Groups](http://groups.google.com/group/mavlink)

This tool is used to connect to an ANIMA system over serial and retrieve logs stored on an SD card. The tool can list available serial ports and queries the user. Once connected, log files may be discovered with the **list** command, and retrieved with the **dumpfile** command. See *Commands* for a full list of commands.

#### Usage ####

       python sd_logreader.py

#### Commands ####

The following commands are available:

> **listing**
>> Lists the size and id number for each log file found on the device.

> **dumpfile** *id*
>> Dumps the file with the given *id*, showing the *id* and size at the top.

> **info**
>> Displays information about the current connection such as port and baud rate.

> **help**
>> Shows a help message listing all of the commands.

> **exit**
>> Quits SDLogReader

