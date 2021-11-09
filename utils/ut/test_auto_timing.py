#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timing_utility import TimingUtility
import unittest

#Usage: nosetest -v test_auto_timing.py to do the test
#Note. Be sure to run 'platform_utility.py init' before the test

"""
    Test case in the auto test scope:
        test_1pps_priority
        test_frequency_priority
        test_revertive
"""
class TestTimingMethods(unittest.TestCase):
    def setUp(self):
        self.timing_instance = TimingUtility()

    def test_1pps_priority(self):
        #set priority and read back to check the value is set
        self.timing_instance.set_1pps_priority('GPS-1PPS', 4)
        self.timing_instance.set_1pps_priority('PTP-1PPS', 3)
        self.timing_instance.set_1pps_priority('SMA-1PPS', 2)
        self.timing_instance.set_1pps_priority('ToD-1PPS', 1)

        ret = self.timing_instance.get_1pps_priority('GPS-1PPS')
        self.assertEqual(ret['priority'], 4)
        ret = self.timing_instance.get_1pps_priority('PTP-1PPS')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_1pps_priority('SMA-1PPS')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_1pps_priority('ToD-1PPS')
        self.assertEqual(ret['priority'], 1)

        #set priority and read back to check the value is set
        self.timing_instance.set_1pps_priority('GPS-1PPS', 1)
        self.timing_instance.set_1pps_priority('PTP-1PPS', 2)
        self.timing_instance.set_1pps_priority('SMA-1PPS', 3)
        self.timing_instance.set_1pps_priority('ToD-1PPS', 4)

        ret = self.timing_instance.get_1pps_priority('GPS-1PPS')
        self.assertEqual(ret['priority'], 1)
        ret = self.timing_instance.get_1pps_priority('PTP-1PPS')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_1pps_priority('SMA-1PPS')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_1pps_priority('ToD-1PPS')
        self.assertEqual(ret['priority'], 4)

        result = 0b00000000
        #get all priority
        ret = self.timing_instance.get_1pps_priorities()
        print(ret[0]['input'])
        for i in range(len(ret)):
            if ret[i]['input'] == 'GPS-1PPS':
                if ret[i]['priority'] == 1:
                    result |= 0b00000001
            elif ret[i]['input'] == 'PTP-1PPS':
                if ret[i]['priority'] == 2:
                    result |= 0b00000010
            elif ret[i]['input'] == 'SMA-1PPS':
                if ret[i]['priority'] == 3:
                    result |= 0b00000100
            elif ret[i]['input'] == 'ToD-1PPS':
                if ret[i]['priority'] == 4:
                    result |= 0b00001000
            else:
                self.assertTrue(False)
        self.assertEqual(result, 0b00001111)

    def test_frequency_priority(self):
        #set priority and read back to check the value is set
        self.timing_instance.set_frequency_priority('GPS-10MHz', 8)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN1', 7)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN2', 6)
        self.timing_instance.set_frequency_priority('SyncE-BCM82780-10G', 5)
        self.timing_instance.set_frequency_priority('SyncE-BCM88470-10G', 4)
        self.timing_instance.set_frequency_priority('PTP-10MHz', 3)
        self.timing_instance.set_frequency_priority('SMA-10MHz', 2)
        self.timing_instance.set_frequency_priority('BITS', 1)

        ret = self.timing_instance.get_frequency_priority('GPS-10MHz')
        self.assertEqual(ret['priority'], 8)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-PIN1')
        self.assertEqual(ret['priority'], 7)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-PIN2')
        self.assertEqual(ret['priority'], 6)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82780-10G')
        self.assertEqual(ret['priority'], 5)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM88470-10G')
        self.assertEqual(ret['priority'], 4)
        ret = self.timing_instance.get_frequency_priority('PTP-10MHz')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_frequency_priority('SMA-10MHz')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_frequency_priority('BITS')
        self.assertEqual(ret['priority'], 1)

        #set priority and read back to check the value is set
        self.timing_instance.set_frequency_priority('GPS-10MHz', 1)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN1', 2)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN2', 3)
        self.timing_instance.set_frequency_priority('SyncE-BCM82780-10G', 4)
        self.timing_instance.set_frequency_priority('SyncE-BCM88470-10G', 5)
        self.timing_instance.set_frequency_priority('PTP-10MHz', 6)
        self.timing_instance.set_frequency_priority('SMA-10MHz', 7)
        self.timing_instance.set_frequency_priority('BITS', 8)

        ret = self.timing_instance.get_frequency_priority('GPS-10MHz')
        self.assertEqual(ret['priority'], 1)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-1')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-2')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82780-10G')
        self.assertEqual(ret['priority'], 4)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM88470-10G')
        self.assertEqual(ret['priority'], 5)
        ret = self.timing_instance.get_frequency_priority('PTP-10MHz')
        self.assertEqual(ret['priority'], 6)
        ret = self.timing_instance.get_frequency_priority('SMA-10MHz')
        self.assertEqual(ret['priority'], 7)
        ret = self.timing_instance.get_frequency_priority('BITS')
        self.assertEqual(ret['priority'], 8)

        result = 0b00000000
        #get all priority
        ret = self.timing_instance.get_frequency_priorities()
        for i in range(len(ret)):
            if ret[i]['input'] == 'GPS-10MHz':
                if ret[i]['priority'] == 1:
                    result |= 0b00000001
            elif ret[i]['input'] == 'SyncE-BCM82398-100G-1':
                if ret[i]['priority'] == 2:
                    result |= 0b00000010
            elif ret[i]['input'] == 'SyncE-BCM82398-100G-2':
                if ret[i]['priority'] == 3:
                    result |= 0b00000100
            elif ret[i]['input'] == 'SyncE-BCM82780-10G':
                if ret[i]['priority'] == 4:
                    result |= 0b00001000
            elif ret[i]['input'] == 'SyncE-BCM88470-10G':
                if ret[i]['priority'] == 5:
                    result |= 0b00010000
            elif ret[i]['input'] == 'PTP-10MHz':
                if ret[i]['priority'] == 6:
                    result |= 0b00100000
            elif ret[i]['input'] == 'SMA-10MHz':
                if ret[i]['priority'] == 7:
                    result |= 0b01000000
            elif ret[i]['input'] == 'BITS':
                if ret[i]['priority'] == 8:
                    result |= 0b10000000
            else:
                self.assertTrue(False)

        self.assertEqual(result, 0b11111111)

    def test_frequency_priority_dpll3(self):
        #set priority and read back to check the value is set
        self.timing_instance.set_frequency_priority('GPS-10MHz-DPLL3', 7)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN1-DPLL3', 6)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN2-DPLL3', 5)
        self.timing_instance.set_frequency_priority('SyncE-BCM82780-10G-DPLL3', 4)
        self.timing_instance.set_frequency_priority('SyncE-BCM88470-10G-DPLL3', 3)
        self.timing_instance.set_frequency_priority('SMA-10MHz-DPLL3', 2)
        self.timing_instance.set_frequency_priority('BITS-DPLL3', 1)

        ret = self.timing_instance.get_frequency_priority('GPS-10MHz-DPLL3')
        self.assertEqual(ret['priority'], 7)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-PIN1-DPLL3')
        self.assertEqual(ret['priority'], 6)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-PIN2-DPLL3')
        self.assertEqual(ret['priority'], 5)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82780-10G-DPLL3')
        self.assertEqual(ret['priority'], 4)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM88470-10G')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_frequency_priority('SMA-10MHz-DPLL3')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_frequency_priority('BITS-DPLL3')
        self.assertEqual(ret['priority'], 1)

        #set priority and read back to check the value is set
        self.timing_instance.set_frequency_priority('GPS-10MHz-DPLL3', 1)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN1-DPLL3', 2)
        self.timing_instance.set_frequency_priority('SyncE-BCM82398-100G-PIN2-DPLL3', 3)
        self.timing_instance.set_frequency_priority('SyncE-BCM82780-10G-DPLL3', 4)
        self.timing_instance.set_frequency_priority('SyncE-BCM88470-10G-DPLL3', 5)
        self.timing_instance.set_frequency_priority('SMA-10MHz-DPLL3', 6)
        self.timing_instance.set_frequency_priority('BITS-DPLL3', 7)

        ret = self.timing_instance.get_frequency_priority('GPS-10MHz-DPLL3')
        self.assertEqual(ret['priority'], 1)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-1-DPLL3')
        self.assertEqual(ret['priority'], 2)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82398-100G-2-DPLL3')
        self.assertEqual(ret['priority'], 3)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM82780-10G-DPLL3')
        self.assertEqual(ret['priority'], 4)
        ret = self.timing_instance.get_frequency_priority('SyncE-BCM88470-10G-DPLL3')
        self.assertEqual(ret['priority'], 5)
        ret = self.timing_instance.get_frequency_priority('SMA-10MHz-DPLL3')
        self.assertEqual(ret['priority'], 6)
        ret = self.timing_instance.get_frequency_priority('BITS-DPLL3')
        self.assertEqual(ret['priority'], 7)

        result = 0b00000000
        #get all priority
        ret = self.timing_instance.get_frequency_priorities()
        for i in range(len(ret)):
            if ret[i]['input'] == 'GPS-10MHz-DPLL3':
                if ret[i]['priority'] == 1:
                    result |= 0b00000001
            elif ret[i]['input'] == 'SyncE-BCM82398-100G-1-DPLL3':
                if ret[i]['priority'] == 2:
                    result |= 0b00000010
            elif ret[i]['input'] == 'SyncE-BCM82398-100G-2-DPLL3':
                if ret[i]['priority'] == 3:
                    result |= 0b00000100
            elif ret[i]['input'] == 'SyncE-BCM82780-10G-DPLL3':
                if ret[i]['priority'] == 4:
                    result |= 0b00001000
            elif ret[i]['input'] == 'SyncE-BCM88470-10G-DPLL3':
                if ret[i]['priority'] == 5:
                    result |= 0b00010000
            elif ret[i]['input'] == 'SMA-10MHz-DPLL3':
                if ret[i]['priority'] == 6:
                    result |= 0b00100000
            elif ret[i]['input'] == 'BITS-DPLL3':
                if ret[i]['priority'] == 7:
                    result |= 0b01000000
            else:
                self.assertTrue(False)

        self.assertEqual(result, 0b01111111)

    def test_revertive(self):
        #enable revertive
        self.timing_instance.set_revertive(1)
        ret = self.timing_instance.get_revertive()
        self.assertEqual(ret['revertive'], 1)

        #disable revertive
        self.timing_instance.set_revertive(0)
        ret = self.timing_instance.get_revertive()
        self.assertEqual(ret['revertive'], 0)

if __name__ == '__main__':
    unittest.main()
