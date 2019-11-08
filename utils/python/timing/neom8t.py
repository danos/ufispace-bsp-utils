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
'''
NEOM8T:
Use USB to write messages and use I2C to read messages
'''

import os
import sys
import time
import serial

from common.logger import Logger
from timing.gpsusb import GPSUSB
from timing.ubx.ubx_cfg_tp5 import UBX_CFG_TP5

TIMEPULSE1 = 0
TIMEPULSE2 = 1

class NEOM8T:

    def __init__(self):
        log = Logger(__name__)
        self.logger = log.getLogger()

    def __del__(self):
        pass

    def init(self):
        usb_dev = GPSUSB()
        # Disable NMEA to make reading UBX response possible to imeplement
        usb_dev.disableNMEAMessage()
        # Workaround:
        # Read all data from buffer before get/set to ensure UBX reponse could be read
        usb_dev.clearBuffer()

        # Configure time pluse 2 to output 10MHz
        usb_dev.configureTimePulse2()

    def deinit(self):
        pass

    def setAntennaCableDelay(self, delay):
        usb_dev = GPSUSB()
        usb_dev.enable()
        # Configuring cable delay for one timepulse will affect both timepulses.
        # Note: For other configurations, it should be checked when implementing.
        for i in [TIMEPULSE1]:#, TIMEPULS2]:
            tpCfg = usb_dev.getTimePulseCfg(i)

            tpCmd = UBX_CFG_TP5(tpCfg)
            tpCmd.setAntennaCableDelay(delay)

            usb_dev.configureTimePulse(tpCmd.getMessage())

    def getAntennaCableDelay(self):
        usb_dev = GPSUSB()
        usb_dev.enable()
        # The cable delay for both timepulses is the same
        tpCfg = usb_dev.getTimePulseCfg(TIMEPULSE1)

        tpCmd = UBX_CFG_TP5(tpCfg)
        return tpCmd.getAntennaCableDelay()

    def setGPSToDTimingFormat(self):
        ser = serial.Serial()
        ser.port = "/dev/ttyACM0"
        ser.baudrate = 9600
        ser.timeout = 1
        ser.open()

        data = ["B56206010800F0020000000000000131",
                "B56206010800F001000000000001012B",
                "B56206010800F0020000000000010232",
                "B56206010800F0030000000000010339",
                "B56206010800F004010000010101074B",
                "B56206010800F0050000000000010547",
                "B56206010800F006000000000000054D",
                "B56206010800F0070000000000000654",
                "B56206010800F0000000000000010024",
                "B562061714000040000200000000000100010000000000000000754F"]

        for x in data:
            ser.write(bytes.fromhex(x))

        ser.flush()
        ser.close()
