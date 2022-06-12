import os, sys, optparse

LOGFILE = "setupapi.dev.log"
KEYWORD1 = "[Device Install (Hardware initiated)"
KEYWORD2 = "USBSTOR"

with open(LOGFILE, "r") as in_file:
    for line in in_file:
        if KEYWORD1 in line and KEYWORD2 in line:
            dev_info_1 = line.split("#")[1].split("&")
            dev_info_2 = line.split("#")[2]
            print(f"\nVendor ID: {dev_info_1[1]}")
            print(f"Product ID: {dev_info_1[2]}")
            print(f"Revision: {dev_info_1[3]}")
            print(f"Serial number: {dev_info_2}")
            print("Timestamp: ", next(in_file).split("start")[1].strip())
