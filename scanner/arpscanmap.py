#!/usr/bin/env python3
import subprocess
import uuid
import re
import netifaces

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

def arpscanmap():
    print('[+] MAC ADDRESS    \tIP Addr    \tVendor')
    print('[+] -----------    \t-------    \t------')
    lst = netifaces.interfaces()
    for interface in lst:
        if interface != 'lo':
            try:
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    adif = link['addr'].split('.')
                    range = '{}.{}.{}.0/24'.format(adif[0], adif[1], adif[2])

                try:
                    dip = []
                    dmac = []
                    scan = subprocess.getoutput('nmap ' + range + ' -n -sP')
                    for data in scan.split('\n'):
                        if 'report' in data:
                            ip = data.split(' ')[4]
                            dip.append(ip)
                        if 'MAC' in data:
                            mac = data.split(' ')[2]
                            dmac.append(mac)

                    no = 0
                    for ip in dip:
                        try:
                            print('[+] ' + dmac[no] + '\t' + ip + '    \t' + checker(dmac[no]))
                        except:
                            mac_addr = uuid.getnode()
                            mek = str(":".join(re.findall('..', '%012x' % mac_addr)))
                            print('[+] ' + mek + '\t' + ip + '    \t' + checker(mek))
                        no = no + 1
                except KeyboardInterrupt: print('\r[!] Exiting program...')
            except: pass
