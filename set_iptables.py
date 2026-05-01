#!/usr/bin/env python3
import subprocess
import argparse

def set_pytables():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--remote", dest="remote", help="Test against a remote Target.")
    parser.add_argument("-l", "--local", dest="local", help="Set IP Tables.")
    parser.add_argument("-n", "--number", dest="number", help="iptables number to set.")
    parser.add_argument("-f", "--flush", dest="flush", help="Flush the iptables.")
    options = parser.parse_args()

    if options.number:
        number = options.number
        print("[+] Request to set iptables to: " + number)
        if options.remote:
            print("[+] Test to remote target using FORWARD.")
            subprocess.call(
                ["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        elif options.local:
            print("[+] Test locally using INPUT and OUTPUT.")
            subprocess.call(["sudo", "iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
            subprocess.call(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        print("[+] Check the iptables have been set:\n")
        subprocess.call(["sudo", "iptables", "-L"])

    elif options.flush:
        subprocess.call(["sudo", "iptables", "--flush"])
        print("[+] Flush iptables.")
        print("[+] Check if the iptables have been flushed.\n")
        subprocess.call(["sudo", "iptables", "-L"])

print("\n[+] Hello, this is set_iptables.  Keep smiling!")
set_pytables()