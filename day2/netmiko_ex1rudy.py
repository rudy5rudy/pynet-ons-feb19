#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler


#def save_file(filename, show_run):
#    """Save the show run to a file"""
#    with open(filename, "w") as f:
#        f.write(show_run)


def main():
    """Exercises using Netmiko"""
    password = getpass()
    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    netconnect = ConnectHandler(**cisco3)
    print(netconnect.find_prompt())
    output = netconnect.send_command("show ver")
    print(output)
    output = netconnect.send_command("show run")
    print(output)

    save_file("cisc003.txt",output)



#write the file
 
def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)


main()
#save_file()
