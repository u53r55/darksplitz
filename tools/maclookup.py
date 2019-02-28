#!/usr/bin/env python3

def checker(macadd):
    try:
        oui = open('dict/mac.txt').read().split('\n')
        mac = macadd.split(':')
        mac = mac[0].upper() + ':' + mac[1].upper() + ':' + mac[2].upper()
        vendor = ''
        for ouis in oui:
            if mac in ouis:
                vendor = ouis.split('|')[1]
        if vendor == '':
            vendor = 'Unknow'
        print('[+] ' + macadd + ' => ' + vendor)
    except: pass

def filecheck(file):
    fil = open(file, 'r').read().split('\n')
    for mac in fil:
        checker(mac)