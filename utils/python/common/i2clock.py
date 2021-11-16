#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################################
#Copyright 2021 Ufi Space Co.,Ltd.                                        #
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
import fcntl
from const.const import SWLock
from time import sleep

def exclusive_i2clock(fn):
    f = fn
    count = 0
    max_retry = 10
    wait_interval = 1
    fd = None
    
    def wrapped_func(*args, **kwargs):
        try:
            fd = open(SWLock.I2C_LOCK_PATH, 'r')
        except IOError:
            fd = open(SWLock.I2C_LOCK_PATH, 'wb')

        for count in range(0, max_retry + 1):
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                # Break here because we should already get lock
                break
            except:
                if count == max_retry:
                    fd.close()
                    raise Exception("Cannot acquire I2C exclude lock after 10s retry")
                sleep(wait_interval)
        try:
            return f(*args, **kwargs)
        except:
            raise
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            fd.close()
            
    return wrapped_func

def shared_i2clock(fn):
    f = fn
    count = 0
    max_retry = 10
    wait_interval = 1
    fd = None
    
    def wrapped_func(*args, **kwargs):
        try:
            fd = open(SWLock.I2C_LOCK_PATH, 'r')
        except IOError:
            fd = open(SWLock.I2C_LOCK_PATH, 'wb')

        for count in range(0, max_retry + 1):
            try:
                fcntl.flock(fd, fcntl.LOCK_SH | fcntl.LOCK_NB)
                
                # Break here because we should already get lock
                break
            except:
                if count == max_retry:
                    raise Exception("Cannot acquire I2C exclude lock after 10s retry")
                sleep(wait_interval)
        try:
            return f(*args, **kwargs)
        except:
            raise
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            fd.close()
            
    return wrapped_func
