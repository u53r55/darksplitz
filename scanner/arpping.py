#!/usr/bin/env python3
from scapy.all import *
import ipaddress

def checker(mac):
    oui = open('dict/mac.txt').read().split('\n')
    mac = mac.split(':')
    mac = mac[0].upper() + ':' + mac[1].upper() + ':' + mac[2].upper()
    vendor = ''
    for ouis in oui:
        if mac in ouis:
            vendor = ouis.split('|')[1]

    if vendor == '':
        vendor = 'Unknow'

    return vendor

def arpping(rang):
    if os.getuid() != 0:
        print('[!] Need to run as root')
        return False

    try: net = ipaddress.IPv4Network(rang)
    except:
        print('[!] Range invalid...')
        return False

    print('[+] MAC ADDRESS    \tIP Addr    \tVendor')
    print('[+] -----------    \t-------    \t------')
    try:
        ans,unans = arping(rang, verbose=0)
        for s,r in ans:
            print("[+] {}\t{}    \t{}".format(r[Ether].src, s[ARP].pdst, checker(r[Ether].src)))

    except: print('\r[!] Invalid address...')