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
                     0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 0x01, 0x00,
                     0x00, 0x00, 0x80, 0x96, 0x98, 0x00, 0x00, 0x00,
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00,
                     0x00, 0x00, 0xEF, 0x00, 0x00, 0x00, 0xA9, 0xA8]
                )

