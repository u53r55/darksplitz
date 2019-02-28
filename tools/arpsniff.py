#!/usr/bin/env python3
from scapy.all import *
import os

device = []
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

def arp_monitor_callback(pkt):
    global device
    if ARP in pkt and pkt[ARP].op in (1,2):
        mac = pkt.sprintf('%ARP.hwsrc%')
        ip = pkt.sprintf('%ARP.psrc%')
        if mac not in device:
            device.append(mac)
            print('[+] {}\t{}    \t{}'.format(mac, ip, checker(mac)))

def arpsniff():
    if os.getuid() != 0:
        print('[!] Need to run as root')
        return False

    print('[+] MAC ADDRESS    \tIP Addr    \tVendor')
    print('[+] -----------    \t-------    \t------')
    sniff(prn=arp_monitor_callback, filter="arp", store=0)
    print('\r[!] Sniffing stoped...')