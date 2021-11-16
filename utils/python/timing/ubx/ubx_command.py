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
import array

class UBXCommand:

    # Default configuration for TimePulse2 to output 10MHz
    cmdCfgTP2 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x31, 0x20, 0x00, 0x01, 0x01,
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,
                     0x00, 0x00, 0x80, 0x96, 0x98, 0x00, 0x00, 0x00,
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00,
                     0x00, 0x00, 0xEF, 0x00, 0x00, 0x00, 0x77, 0x30]
                )
    # Timemode 2 / Disabled
    cmdCfgTimeMode2 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x3D, 0x1C, 0x00, 0x00, 0x00,
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                     0x00, 0x00, 0x5F, 0x6B]
                )
    
    # Output ToD from Uart    
    cmdCfgTod1 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x02, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x31],
                 )
                 
    cmdCfgTod2 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x01, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x2B]
                 )
                 
    cmdCfgTod3 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x02, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x32]
                 )

    cmdCfgTod4 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x03, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x39],
                 )

    cmdCfgTod5 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x04, 
                     0x01, 0x00, 0x00, 0x01, 0x01, 0x01, 0x07, 0x4B]
                 )

    cmdCfgTod6 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x05, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x05, 0x47]
                 )

    cmdCfgTod7 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x06, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x4D]
                 )

    cmdCfgTod8 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x07, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x54]
                 )

    cmdCfgTod9 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x00, 
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x24]
                 )

    cmdCfgTod10 = array.array('B',
                    [0xB5, 0x62, 0x06, 0x17, 0x14, 0x00, 0x00, 0x40, 
                     0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 
                     0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                     0x00, 0x00, 0x75, 0x4F]
                 )
    # Enable Uart to output ZDA NMEA
    cmdCfgUartZDAEn = array.array('B',
                    [0xB5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x08, 
                     0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x09, 0x63]
                )
