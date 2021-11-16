#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from timing_utility import TimingUtility
from cpld.cpld import CPLD
from CPLD_utility import CPLDUtility
from Reset_utility import ResetUtility
from Interrupt_utility import InterruptUtility

def main():
    print("Test Timing Utilities")
    util = TimingUtility()
    cpldutil = CPLDUtility()
    resetutil = ResetUtility()
    intrutil = InterruptUtility()
    cpld = CPLD()
    if sys.argv[1] == "1":
        util.set_1pps_priority(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == "2":
        util.set_frequency_priority(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == "3":
        util.set_frequency_priority_dpll3(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == "4":
        print(util.get_1pps_priority(sys.argv[2]))
    elif sys.argv[1] == "5":
        print(util.get_1pps_priorities())
    elif sys.argv[1] == "6":
        print(util.get_frequency_priority(sys.argv[2]))
    elif sys.argv[1] == "7":
        print(util.get_frequency_priority_dpll3(sys.argv[2]))
    elif sys.argv[1] == "8":
        print(util.get_frequency_priorities())
    elif sys.argv[1] == "9":
        print(util.get_frequency_priorities_dpll3())
    elif sys.argv[1] == "10":
        util.set_revertive(int(sys.argv[2]))
    elif sys.argv[1] == "11":
        print(util.get_revertive())
    elif sys.argv[1] == "12":
        print(util.get_dpll_disqualified_inputs())
    elif sys.argv[1] == "13":
        util.clear_dpll_interrupts()
    elif sys.argv[1] == "14":
        print(util.get_dpll_input_status(sys.argv[2]))
    elif sys.argv[1] == "15":
        print(util.get_dpll_status(int(sys.argv[2])))
    elif sys.argv[1] == "16":
        print(util.get_bits_status())
    elif sys.argv[1] == "17":
        print(util.enable_dpll_interrupt_mask(sys.argv[2]))
    elif sys.argv[1] == "18":
        print(util.disable_dpll_interrupt_mask(sys.argv[2]))
    elif sys.argv[1] == "19":
        print(util.get_dpll_interrupt_mask())
    elif sys.argv[1] == "20":
        print(cpld.interrupt_mask_enable(sys.argv[2]))
    elif sys.argv[1] == "21":
        print(cpld.interrupt_mask_disable(sys.argv[2]))
    elif sys.argv[1] == "22":
        print(cpld.interrupt_mask_get())
    elif sys.argv[1] == "23":
        print(cpld.host_status_smbus_alert_clear())
    elif sys.argv[1] == "24":
        print(cpldutil.get_bmc_power_status())
    elif sys.argv[1] == "25":
        print(resetutil.set_bcm_reset_mask(sys.argv[2]))
    elif sys.argv[1] == "26":
        print(resetutil.unset_bcm_reset_mask(sys.argv[2]))
    elif sys.argv[1] == "27":
        print(resetutil.set_mux_reset_mask(sys.argv[2]))
    elif sys.argv[1] == "28":
        print(resetutil.unset_mux_reset_mask(sys.argv[2]))
    elif sys.argv[1] == "29":
        print(intrutil.get_nmi_interrupt())
    elif sys.argv[1] == "30":
        print(cpldutil.enable_power_ctrl_mask(sys.argv[2]))
    elif sys.argv[1] == "31":
        print(cpldutil.disable_power_ctrl_mask(sys.argv[2]))
    elif sys.argv[1] == "32":
        print(intrutil.enable_smbus_interrupt())
    elif sys.argv[1] == "33":
        print(intrutil.disable_smbus_interrupt())
    elif sys.argv[1] == "34":
        cpldutil.set_tod_output(int(sys.argv[2]))
    elif sys.argv[1] == "35":
        util.set_gps_tod_timing_format()
    elif sys.argv[1] == "36":
        util.set_synce_select_option(int(sys.argv[2]))
    elif sys.argv[1] == "37":
        util.set_bits_t1e1_selection(int(sys.argv[2]))
    elif sys.argv[1] == "38":
        util.set_dpll_fast_lock(int(sys.argv[2]))
    elif sys.argv[1] == "39":
        print(util.get_input_clock_phase_offset(sys.argv[2]))
    elif sys.argv[1] == "40":
        util.set_input_clock_phase_offset(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == "41":
        util.set_dpll1_output_offset(int(sys.argv[2]))
    elif sys.argv[1] == "42":
        util.set_dpll2_output_offset(int(sys.argv[2]))
    elif sys.argv[1] == "43":
        util.set_dpll_op_mode(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "44":
        util.set_dpll_hitless_mode(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "45":
        util.set_gps_tm_surveyin(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "46":
        util.set_gps_tm_fixed (int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5]))
    elif sys.argv[1] == "47":
        util.set_gps_tm_disable()
    else:
        print("Error input!!")

if __name__ == "__main__":
    main()
