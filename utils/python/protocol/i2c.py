#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################################
#Copyright 2020 Ufi Space Co.,Ltd.                                        #
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
from smbus import SMBus

from common.logger import Logger

class I2C:
    I2C_DEV_CHK = [[
        {"name": "CPU EEPROM", "addr": 0x57},
        {"name": "CPU TMP75", "addr": 0x4f}
    ]]

    def __init__(self, busnum=0):
        log = Logger(__name__)
        self.logger = log.getLogger()
        self.busnum = busnum

    def check_status(self):
        try:
            bus = SMBus(self.busnum)
            if self.busnum >= len(self.I2C_DEV_CHK):
                self.logger.error("Bad I2C bus num: " + str(self.busnum))
                return False

            # Try to read i2c devices to check bus health
            for dev in self.I2C_DEV_CHK[self.busnum]:
                bus.read_byte(dev["addr"])
            
            return True
        except Exception as e:
            self.logger.error("Bad I2C bus " + str(self.busnum) + " status, err: " + repr(e))
            return False
        finally:
            if bus != None:
                bus.close()

