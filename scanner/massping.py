#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
import subprocess
import ipaddress
import time
import sys

def pings(ip):
    run = subprocess.getoutput('ping -c 1 -w 1 {}'.format(ip))
    if '1 received' in run:
        sys.stdout.write('[+] {}\n'.format(ip))

def massping(range):
    try: net = ipaddress.IPv4Network(range)
    except:
        print('[!] Invalid address')
        return False
    executor = ThreadPoolExecutor(max_workers=1000)
    futures = []
    for ip in net:
        a = executor.submit(pings, ip)
        futures.append(a)
    while True:
        if a.done() == True:
            time.sleep(1)
            break
