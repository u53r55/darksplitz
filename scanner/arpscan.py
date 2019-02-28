#!/usr/bin/python3
import sys, ipaddress, time, psutil, os, netifaces
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor

def prog():
    sys.stdout.flush()
    sys.stdout.write('[+] Scanning...\r')
    sys.stdout.flush()
    sys.stdout.write('[x] Scanning...\r')

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

def scanner(iface, ip):
    try:
        prog()
        alive, dead = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), iface=iface, timeout=3, verbose=0)
        mac = str(alive[0][1].hwsrc)
        sys.stdout.write('[+] ' + mac + '\t' + ip + '    \t' + checker(mac) + '\n')
    except: pass

def arpscan():
    if os.getuid() != 0:
        print('[!] Need to run as root')
        return False

    print('[+] MAC ADDRESS    \tIP Addr    \tVendor')
    print('[+] -----------    \t-------    \t------')
    lst = netifaces.interfaces()
    for interface in lst:
        if interface != 'lo':
            try:
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    adif = link['addr'].split('.')
                    ips = '{}.{}.{}.0/24'.format(adif[0], adif[1], adif[2])

                try:
                    executor = ThreadPoolExecutor(max_workers=100)
                    futures = []
                    ip = ipaddress.IPv4Network(ips)
                    for ipadd in ip:
                        try:
                            a = executor.submit(scanner, interface, str(ipadd))
                            futures.append(a)
                        except KeyboardInterrupt: break

                    while True:
                        cek = a.done()
                        if cek == True:
                            time.sleep(1)
                            break

                except KeyboardInterrupt: print('\r[!] Exiting program...')
            except: pass