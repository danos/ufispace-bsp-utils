#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################################
#Copyright 2019 Ufi Space Co.,Ltd.                                        #
#                                                                         #
#Licensed under the Apache License, Version 2.0 (the "License");          #
#you may not use this file except in compliance with the License.         #
#You may obtain a copy of the License at                                  #
#                                                                         #
#    http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                         #
#Unless required by applicable law or agreed to in writing, software      #
#distributed under the License is distributed on an "AS IS" BASIS,        #
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#See the License for the specific language governing permissions and      #
#limitations under the License.                                           #
###########################################################################
import os
import sys

from common.logger import Logger
from i2c_mux.i2c_mux import I2CMux
from gpio.ioexp import IOExpander
from smbus import SMBus
from cpld.cpld import CPLD
from protocol.i2c import I2C

class DATA_INFO:
    SFP = {
        "list":[
            ["Identifier",   1, "hex"],
            ["Extend_ID",    1, "dec"],
            ["Connector",    1, "hex"],
            ["Transceiver",  8, "str"],
            ["Encoding",     1, "dec"],
            ["Baudrate",     1, "dec"],
            ["Rate_ID",      1, "dec"],
            ["Length_9u_km", 1, "dec"],
            ["Length_9u",    1, "dec"],
            ["Length_50u",   1, "dec"],
            ["Length_62_5u", 1, "dec"],
            ["Length_Cu",    1, "dec"],
            ["reserve2",     1, "hex"],
            ["Vendor_Nme",  16, "str"],
            ["reserve3",     1, "hex"],
            ["Vendor_OUI",   3, "hex"],
            ["Vendor_PN",   16, "str"],
            ["vendor_Rev",   4, "hex"],
            ["Wavelength",   2, "hex"],
            ["reserve4",     1, "hex"],
            ["CC_Base",      1, "dec"],
            ["Options",      2, "hex"],
            ["BR_Max",       1, "dec"],
            ["BR_Min",       1, "dec"],
            ["Serial_No",   16, "str"],
            ["Date_Code",    8, "str"],
            ["reserve5",     3, "hex"],
            ["CC_ext",       1, "dec"],
            ["Vendor_Specific", 16, "str"]            
        ]
    }
    
    QSFP = {
        "list":[
            ["Low_Memory",         127, "str"],
            ["Page_Sel",             1, "hex"],
            ["Identifier",           1, "hex"],
            ["Extend_ID",            1, "dec"],
            ["Connector",            1, "hex"],
            ["Transceiver",          8, "str"],
            ["Encoding",             1, "dec"],
            ["Baudrate",             1, "dec"],
            ["Ext_Baudrate",         1, "dec"],
            ["Length_smf",           1, "dec"],
            ["Length_e_50u",         1, "dec"],
            ["Length_50u",           1, "dec"],
            ["Length_62_5u",         1, "dec"],
            ["Length_Cu",            1, "dec"],
            ["dev_tech",             1, "hex"],
            ["Vendor_Nme",          16, "str"],
            ["Ext_Transceiver",      1, "hex"],
            ["Vendor_OUI",           3, "hex"],
            ["Vendor_PN",           16, "str"],
            ["vendor_Rev",           2, "hex"],
            ["Wavelength",           2, "hex"],
            ["Wavelength_tolerance", 2, "hex"],
            ["Max_case_temp",        1, "dec"],
            ["CC_base",              1, "dec"],
            ["Options",              4, "hex"],
            ["Serial_No",           16, "str"],
            ["Date_Code",            8, "str"],
            ["Diag_Mon_Type",        1, "hex"],
            ["Enhanced_Option",      1, "hex"],
            ["reserve",              1, "hex"],
            ["CC_ext",               1, "dec"],
            ["Vendor_Specific",     32, "str"]            
        ]
    }

class EEPRom:

    PATH_SYS_I2C_DEVICES = "/sys/bus/i2c/devices"

    I2C_BUS_CPU_EEPROM = 0

    I2C_ADDR_MUX_9546 = 0x76
    I2C_ADDR_QSFP_MUX_9546 = 0x70
    I2C_ADDR_SFP_MUX_9548_1 = 0x71
    I2C_ADDR_SFP_MUX_9548_2 = 0x72
    I2C_ADDR_SFP_MUX_9548_3 = 0x73
    I2C_ADDR_SFP_MUX_9548_4 = 0x74

    I2C_ADDR_EEPROM_Alpha_CPU  = 0x51
    I2C_ADDR_EEPROM_Beta_CPU  = 0x57
    I2C_ADDR_EEPROM_SFP_A0  = 0x50
    I2C_ADDR_EEPROM_SFP_A2  = 0x51
    I2C_ADDR_EEPROM_QSFP_A0 = 0x50
    I2C_ADDR_EEPROM_QSFP_A2 = 0x51

    CPU_EEPROM_SIZE = 256
    CPU_EEPROM_PAGE_SIZE = 0x10
    CPU_EEPROM_PAGE_MASK = CPU_EEPROM_PAGE_SIZE - 1
    
    SFP_QSFP_CHANEL = 0x08
    SFP_EEPROM_SIZE = 256
    SFP_EEPROM_PAGE_SIZE = 0x10
    SFP_EEPROM_PAGE_MASK = SFP_EEPROM_PAGE_SIZE - 1
    QSFP_EEPROM_SIZE = 256
    QSFP_EEPROM_PAGE_SIZE = 0x10
    QSFP_EEPROM_PAGE_MASK = SFP_EEPROM_PAGE_SIZE - 1
    
    def __init__(self):
        log = Logger(__name__)
        self.logger = log.getLogger()
        self.i2c_mux = I2CMux()
        self.ioexp = IOExpander()
        self.cpld = CPLD()
        
    def _data_transfer(self, _len, _type, _data):
        
        output = ""
        if _type == "str":
            for i in range(_len):
                output = output + chr(_data[i])
        elif _type == "hex":
            output = "0x"
            for i in range(_len):
                output = output + hex(_data[i])[2:]
        else:
            for i in range(_len):
                output = output + str(_data[i])

        return output

    def _get_sfp_mux_channel(self, port_num):
        ch = port_num % 8
        # Normal channel conversion
        chanl = 0x1 << ch

        return chanl
        
    def _get_qsfp_mux_channel(self, port_num):
        ch = port_num % 8
        # Customize channel
        if ch == 0:
            chanl = 0x08
        elif ch == 1:
            chanl = 0x04
        else:
            chanl = 0x0

        return chanl
            
    def _get_sfp_mux_addr(self, port_num):
        port_grp = int(port_num / 8)

        if port_grp == 0:      # P0~P7
            mux = self.I2C_ADDR_SFP_MUX_9548_1
        elif port_grp == 1:    # P8~P15
            mux = self.I2C_ADDR_SFP_MUX_9548_2
        elif port_grp == 2:    # P16~P23
            mux = self.I2C_ADDR_SFP_MUX_9548_3
        else:                  # P24~P27
            mux = self.I2C_ADDR_SFP_MUX_9548_4

        return mux

    def init(self):
        pass

    def dump_cpu_eeprom(self):
        try:
            # Get the bus number of sysfs
            bus_num = self.I2C_BUS_CPU_EEPROM
            bus = SMBus(bus_num)

            offset = 0
            data = []
            while offset < self.CPU_EEPROM_SIZE:
                blk_off = offset & self.CPU_EEPROM_PAGE_MASK
                _len = self.CPU_EEPROM_SIZE - offset
                maxlen = self.CPU_EEPROM_PAGE_SIZE - (blk_off & self.CPU_EEPROM_PAGE_MASK)
                if _len > maxlen:
                    _len = maxlen

                # Send device select code
                # Proto and Alpha doesn't have parent MUX
                hw_rev = self.cpld.get_hw_rev()
                if hw_rev == self.cpld.HARDWARE_REV_PROTO_STR:
                    eeprom_addr = self.I2C_ADDR_EEPROM_Alpha_CPU 
                elif hw_rev == self.cpld.HARDWARE_REV_ALPHA_STR:
                    eeprom_addr = self.I2C_ADDR_EEPROM_Alpha_CPU 
                else:
                    eeprom_addr = self.I2C_ADDR_EEPROM_Beta_CPU
                    
                bus.write_byte_data(eeprom_addr, (offset>>8)&0xff, offset&0xff)
                for i in range(_len):
                    res = bus.read_byte(eeprom_addr)
                    data.append(res)

                offset = offset + _len

            return data
        except Exception as e:
            self.logger.error("Dump CPU EEPROM fail, error: " + str(e))
            raise
        finally:
            if bus != None:
                bus.close()

    def dump_sfp_eeprom(self, port_num, page = None):
        try:
            bus = SMBus(0)

            if page == None or page == "A0":
                i2c_address = self.I2C_ADDR_EEPROM_SFP_A0
            elif page == "A2":
                i2c_address = self.I2C_ADDR_EEPROM_SFP_A2
            
            # Enable the channel of PCA9548
            bus.write_byte_data(self.I2C_ADDR_MUX_9546, 0x0, self.SFP_QSFP_CHANEL)
                        
            # Enable the channel by port location
            mux_addr = self._get_sfp_mux_addr(port_num)
            mux_chanl = self._get_sfp_mux_channel(port_num)
            bus.write_byte_data(mux_addr, 0x0, mux_chanl)

            offset = 0
            data = []
            
            # Clean the eeprom internal counter
            bus.write_byte(i2c_address, 0x0)
            
            while offset < self.SFP_EEPROM_SIZE:
                blk_off = offset & self.SFP_EEPROM_PAGE_MASK
                _len = self.SFP_EEPROM_SIZE - offset
                maxlen = self.SFP_EEPROM_PAGE_SIZE - (blk_off & self.SFP_EEPROM_PAGE_MASK)
                if _len > maxlen:
                    _len = maxlen

                for i in range(_len):
                    res = bus.read_byte(i2c_address)
                    data.append(res)

                offset = offset + _len    
                
            data_base = 0
            content = {}
            for j in range(len(DATA_INFO.SFP["list"])):
                
                data_str = []
                data_len = DATA_INFO.SFP["list"][j][1]
                data_type = DATA_INFO.SFP["list"][j][2]
                for k in range(data_len):
                    data_str.append(data[data_base+k])
                
                if ("reserve" not in DATA_INFO.SFP["list"][j][0]) and \
                   ("Vendor_Specific" not in DATA_INFO.SFP["list"][j][0]):
                   content.update({DATA_INFO.SFP["list"][j][0]: self._data_transfer(data_len, data_type, data_str)})
            
                data_base = data_base + data_len     

            return data
        except Exception as e:
            self.logger.error("Dump SFP port(" + str(port_num) + ") EEPROM fail, error: " + str(e))
            ### Error handle
            # Check if we also can't access other i2c devices
            i2c = I2C(0)
            if i2c.check_status() == False:
                self.logger.error("SFP Port "+ str(port_num) + " might have transceiver issue, please check it")
            else:
                self.logger.error("Dump SFP port fail, but other I2C devices is OK")

            #Try to reset i2c mux
            cpld = CPLD()
            cpld.mux_reset_by_sfp_port(port_num)
            raise
        finally:         
            # Disable the channel by port location
            bus.write_byte_data(mux_addr, 0x0, 0x0)
            
            # Disable the channel of PCA9548
            bus.write_byte_data(self.I2C_ADDR_MUX_9546, 0x0, 0x0)
            
            if bus != None:
                bus.close()

    def dump_qsfp_eeprom(self, port_num, page = None):
        try:
            bus = SMBus(0)

            if page == None or page == "A0":
                i2c_address = self.I2C_ADDR_EEPROM_QSFP_A0
            elif page == "A2":
                i2c_address = self.I2C_ADDR_EEPROM_QSFP_A2
            
            # Enable the channel of PCA9548
            bus.write_byte_data(self.I2C_ADDR_MUX_9546, 0x0, self.SFP_QSFP_CHANEL)
                        
            # Enable the channel by port location
            mux_addr = self.I2C_ADDR_QSFP_MUX_9546
            mux_chanl = self._get_qsfp_mux_channel(port_num)
            bus.write_byte_data(mux_addr, 0x0, mux_chanl)
               
            offset = 0
            data = []
            
            # Clean the eeprom internal counter 
            bus.write_byte(i2c_address, 0x0)
            
            while offset < self.QSFP_EEPROM_SIZE:
                blk_off = offset & self.QSFP_EEPROM_PAGE_MASK
                _len = self.QSFP_EEPROM_SIZE - offset
                maxlen = self.QSFP_EEPROM_PAGE_SIZE - (blk_off & self.QSFP_EEPROM_PAGE_MASK)
                if _len > maxlen:
                    _len = maxlen

                for i in range(_len):
                    res = bus.read_byte(i2c_address)
                    data.append(res)

                offset = offset + _len
            
            data_base = 0
            content = {}
            for j in range(len(DATA_INFO.QSFP["list"])):
                
                data_str = []
                data_len = DATA_INFO.QSFP["list"][j][1]
                data_type = DATA_INFO.QSFP["list"][j][2]
                for k in range(data_len):
                    data_str.append(data[data_base+k])
                
                if ("Low_Memory" not in DATA_INFO.QSFP["list"][j][0]) and \
                   ("Page_Sel" not in DATA_INFO.QSFP["list"][j][0]) and \
                   ("Vendor_Specific" not in DATA_INFO.QSFP["list"][j][0]) and \
                   ("dev_tech" not in DATA_INFO.QSFP["list"][j][0]) and \
                   ("Ext_Transceiver" not in DATA_INFO.QSFP["list"][j][0]) and \
                   ("Max_case_temp" not in DATA_INFO.QSFP["list"][j][0]):                    
                   content.update({DATA_INFO.QSFP["list"][j][0]: self._data_transfer(data_len, data_type, data_str)})
            
                data_base = data_base + data_len

            return data
        except Exception as e:
            self.logger.error("Dump QSFP port(" + str(port_num) + ") EEPROM fail, error: " + str(e))

            ### Error handle
            # Check if we also can't access other i2c devices
            i2c = I2C(0)
            if i2c.check_status() == False:
                self.logger.error("QSFP Port "+ str(port_num) + " might have transceiver issue, please check it")
            else:
                self.logger.error("Dump QSFP port fail, but other I2C devices is OK")

            #Try to reset i2c mux
            cpld = CPLD()
            cpld.mux_reset_by_qsfp_port(port_num)
            raise
        finally:
            # Disable the channel by port location
            bus.write_byte_data(mux_addr, 0x0, 0x0)
            
            # Disable the channel of PCA9548
            bus.write_byte_data(self.I2C_ADDR_MUX_9546, 0x0, 0x0)
            
            if bus != None:
                bus.close()
