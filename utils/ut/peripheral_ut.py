#!/usr/bin/env python3

import os
import sys

from CPLD_utility import CPLDUtility
from EEPROM_utility import EEPRomUtility
from QSFP_utility import QSFPUtility
from SFP_utility import SFPUtility


def cpld_usage(cmd):
    print("Usage: " + cmd + " CPLD 1|2|3|4|5|6|help [option1] [option2] [option3] [option4]")
    print("    1: Get board ID")
    print("    2: Get CPLD version")
    print("       option1: 0 for MB, 1 for CPU")
    print("    3: Set UART source")
    print("       option1: 0 for CPU, 1 for BMC")
    print("    4: Get UART source")
    print("    5: Set LED")
    print("       option1: 0 for SYS, 3 for GPS, 4 for SYNC")
    print("       option2: 0 for OFF, 1 for ON")
    print("       option3: 0 for yellow, 1 for green")
    print("       option4: 0 for solid, 1 for blinking")
    print("    6: Get LED status")
    print("       option1: 0 for SYS, 1 for PSU, 2 for FAN, 3 for GPS, 4 for SYNC")
    print("    7: Get board information, including 'board id', 'hardware revision' and 'build revision'")

def ut_cpld(argv):
    try:
        util = CPLDUtility()

        if argv[2] == '1':
            print(util.get_board_id())
        elif argv[2] == '2':
            print(util.get_cpld_version(int(argv[3])))
        elif argv[2] == '3':
            util.set_uart_source(int(argv[3]))
        elif argv[2] == '4':
            print(util.get_uart_source())
        elif argv[2] == '5':
            util.set_led_control(int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]))
        elif argv[2] == '6':
            print(util.get_led_status(int(argv[3])))
        elif argv[2] == '7':
            print(util.get_board_info())
        else:
            cpld_usage(argv[0])
    except:
        raise

def eeprom_usage(cmd):
    print("Usage: " + cmd + " EEPROM 1|2|3|help [option1]")
    print("    1: Dump EEPROM content from CPU")
    print("    2: Dump EEPROM content from specific SFP+ port")
    print("       option1: Port number, 0-27")
    print("    3: Dump EEPROM content from specific QSFP port")
    print("       option1: Port number, 0-1")

def ut_eeprom(argv):
    try:
        util = EEPRomUtility()
        
        if argv[2] == '1':
            print(util.dump_cpu_eeprom())
        elif argv[2] == '2':
            print(util.dump_sfp_eeprom(int(argv[3])))
        elif argv[2] == '3':
            print(util.dump_qsfp_eeprom(int(argv[3])))
        else:
            eeprom_usage(argv[0])
    except:
        raise

def qsfp_usage(cmd):
    print("Usage: " + cmd + " QSFP 1|2|3|4|help [option1] [option2]")
    print("    1: Get QSFP port presence")
    print("       option1: Port number, 0-1")
    print("    2: Set Low Power Mode to QSFP port")
    print("       option1: Port number, 0-1")
    print("       option2: 0 for disable, 1 for enable")
    print("    3: Get Low Power Mode setting of QSFP port")
    print("       option1: Port number, 0-1")
    print("    4: Reset QSFP port")
    print("       option1: Port number, 0-1")

def ut_qsfp(argv):
    try:
        util = QSFPUtility()
        
        if argv[2] == '1':
            print(util.get_presence(int(argv[3])))
        elif argv[2] == '2':
            util.set_lp_mode(int(argv[3]), int(argv[4]))
        elif argv[2] == '3':
            print(util.get_lp_mode(int(argv[3])))
        elif argv[2] == '4':
            util.reset_port(int(argv[3]))
        else:
            qsfp_usage(argv[0])
    except:
        raise

def sfp_usage(cmd):
    print("Usage: " + cmd + " SFP 1|2|3|4|5|6|7|help [option1] [option2]")
    print("    1: Get SFP+ port presence")
    print("       option1: Port number, 0-27")
    print("    2: Get SFP+ port RX Lost")
    print("       option1: Port number, 0-27")
    print("    3: Get SFP+ port TX Fault")
    print("       option1: Port number, 0-27")
    print("    4: Set SFP+ port rate")
    print("       option1: Port number, 0-27")
    print("       option2: 0 for 1G, 1 for 10G")
    print("    5: Get SFP+ port rate")
    print("       option1: Port number, 0-27")
    print("    6: Set SFP+ port status")
    print("       option1: Port number, 0-27")
    print("       option2: 0 for enable, 1 for disable")
    print("    7: Get SFP+ port status setting")
    print("       option1: Port number, 0-27")

def ut_sfp(argv):
    try:
        util = SFPUtility()
        
        if argv[2] == '1':
            print(util.get_presence(int(argv[3])))
        elif argv[2] == '2':
            print(util.get_rx_lost(int(argv[3])))
        elif argv[2] == '3':
            print(util.get_tx_fault(int(argv[3])))
        elif argv[2] == '4':
            util.set_port_rate(int(argv[3]), int(argv[4]))
        elif argv[2] == '5':
            print(util.get_port_rate(int(argv[3])))
        elif argv[2] == '6':
            util.set_port_status(int(argv[3]), int(argv[4]))
        elif argv[2] == '7':
            print(util.get_port_status(int(argv[3])))
        else:
            sfp_usage(argv[0])
    except:
        raise

def main():
    if len(sys.argv) < 2:
        print("\nUsage: " + sys.argv[0] + " CPLD|EEPROM|QSFP|SFP|help")
        return

    if sys.argv[1] == 'CPLD':
        ut_cpld(sys.argv)
    elif sys.argv[1] == 'EEPROM':
        ut_eeprom(sys.argv)
    elif sys.argv[1] == 'QSFP':
        ut_qsfp(sys.argv)
    elif sys.argv[1] == 'SFP':
        ut_sfp(sys.argv)
    elif sys.argv[1] == 'help':
        print("\nUsage: " + sys.argv[0] + " CPLD|EEPROM|QSFP|SFP|help")
    else:
        print("Invalid arguments:")

        # print command line arguments
        for arg in sys.argv[1:]:
            print(arg)
        print("\nUsage: " + sys.argv[0] + " CPLD|EEPROM|QSFP|SFP|help")

if __name__ == "__main__":
    main()

