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
from timing.ubx import ubx_utils

class UBX_CFG_TM2():
    sync_char = [0xB5, 0x62]
    class_id = [0x06, 0x3D]
    length = 28
    maximum_position = 2147483647
    minimum_position = -2147483647
    maximum_pos_accur_value = 4294960
    minimum_obser_time = 4294967295

    def setFixedDelayPayload(self, cmd, accuracy, x, y, z ):
        x = UBX_CFG_TM2.position_check(x)
        y = UBX_CFG_TM2.position_check(y)
        z = UBX_CFG_TM2.position_check(z)
        accuracy = UBX_CFG_TM2.maximum_position_accuracy_check(accuracy)
        cmd[6] = 0x02
        if x < 0:
            x = x & 0xffffffff 
        
        if y < 0:
            y = y & 0xffffffff
        
        if z < 0:
            z = z & 0xffffffff
            

        cmd[10] = x & 0b11111111
        cmd[11] = x >> 8 & 0b11111111
        cmd[12] = x >> 16 & 0b11111111
        cmd[13] = x >> 24 & 0b11111111
        cmd[14] = y & 0b11111111
        cmd[15] = y >> 8 & 0b11111111
        cmd[16] = y >> 16 & 0b11111111
        cmd[17] = y >> 24 & 0b11111111
        cmd[18] = z & 0b11111111
        cmd[19] = z >> 8 & 0b11111111
        cmd[20] = z >> 16 & 0b11111111
        cmd[21] = z >> 24 & 0b11111111
        cmd[22] = accuracy & 0b11111111
        cmd[23] = accuracy >> 8 & 0b11111111
        cmd[24] = accuracy >> 16 & 0b11111111
        cmd[25] = accuracy >> 24 & 0b11111111
        cmd += ubx_utils.getCheckSum(cmd[2:34])

        return cmd

    def setSurInPayload(self, cmd, obtime, accuracy):
        obtime = UBX_CFG_TM2.maximum_obtime_accuracy_check(obtime)
        accuracy = UBX_CFG_TM2.maximum_position_accuracy_check(accuracy)
        cmd[6] = 0x01
        cmd[26] = obtime & 0b11111111
        cmd[27] = obtime >> 8 & 0b11111111
        cmd[28] = obtime >> 16 & 0b11111111
        cmd[29] = obtime >> 24 & 0b11111111
        cmd[30] = accuracy & 0b11111111
        cmd[31] = accuracy >> 8 & 0b11111111
        cmd[32] = accuracy >> 16 & 0b11111111
        cmd[33] = accuracy >> 24 & 0b11111111
        cmd += ubx_utils.getCheckSum(cmd[2:34])
        
        return cmd

    def setSDisablePayload(self, cmd):
        cmd[6] = 0x00
        cmd += ubx_utils.getCheckSum(cmd[2:34])
        
        return cmd

    @staticmethod
    def timeModeCmd():
        data = [0] * UBX_CFG_TM2.length
        cmd = []
        cmd += UBX_CFG_TM2.sync_char
        buf = []
        buf += UBX_CFG_TM2.class_id
        buf += [0x1C, 0x00]
        buf += data
        cmd += buf

        return cmd
        
    def position_check(value):
        if value >= UBX_CFG_TM2.maximum_position:
            return UBX_CFG_TM2.maximum_position
        elif value <= UBX_CFG_TM2.minimum_position:
            return UBX_CFG_TM2.minimum_position
        else:
            return value
    
    def maximum_position_accuracy_check(value):
        if value >= UBX_CFG_TM2.maximum_pos_accur_value:
            return UBX_CFG_TM2.maximum_pos_accur_value
        else:
            return value

    def maximum_obtime_accuracy_check(value):
        if value >= UBX_CFG_TM2.minimum_obser_time:
            return UBX_CFG_TM2.minimum_obser_time
        else:
            return value        
