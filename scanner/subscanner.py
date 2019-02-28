#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
from socket import getaddrinfo
import subprocess, sys, time

def prog():
    sys.stdout.flush()
    sys.stdout.write('[+] Scanning...\r')
    sys.stdout.flush()
    sys.stdout.write('[x] Scanning...\r')

def cekhost(subdomain):
    x = subprocess.getoutput('host ' + subdomain)
    for d in x.split('\n'):
        if 'has address' in d:
            ip = d.split(' ')[3]
            print('[+] ' + ip + '    \t' * 1 + subdomain)

def subscan(domain, file):
    try: cek = getaddrinfo(domain, None)
    except:
        print('[!] Domain not found...')
        return False

    print('[+] IP/Host\t    \tSubdomain')
    print('[+] -------\t    \t---------')
    executor = ThreadPoolExecutor(max_workers=100)
    futures = []
    for sub in open(file, 'r', encoding='ISO-8859-1').read().split('\n'):
        try:
            prog()
            subdomain = sub + '.' + domain
            a = executor.submit(cekhost, subdomain)
            futures.append(a)
        except KeyboardInterrupt:
            print('\r[!] Exiting program...')
            break

    while True:
        try:
            prog()
            cek = a.done()
            if cek == True:
                time.sleep(1)
                print('[+] ------------------------------\r')
                break

        except KeyboardInterrupt:
            print('\r[!] Exiting program...')

def subdomain_scanner_indo(domain):
    subscan(domain, 'dict/indonesia.txt')

def subdomain_scanner_english(domain):
    subscan(domain, 'dict/english.txt')

def subdomain_scanner(domain):
    subscan(domain, 'dict/subdomain.txt')