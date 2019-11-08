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
import logging
import logging.handlers

class Logger:

    def __init__(self, module_name):
        self.log = logging.getLogger(module_name)
        self.log.setLevel(logging.INFO)

        if len(self.log.handlers) == 0:
            handler = logging.handlers.SysLogHandler(address = '/dev/log')
            handler.setLevel(logging.INFO)

            formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

        #if len(self.log.handlers) == 0:
            self.log.addHandler(handler)

    def getLogger(self):
        return self.log
