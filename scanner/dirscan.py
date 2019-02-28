#!/usr/bin/env python3
# Description : DirsPY - Directory Scanner (Python)
# Author : Koboi137 ( Backbox Indonesia )

from datetime import datetime
from time import sleep, strftime
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import requests, sys, urllib3, argparse
import os, resource

class cl:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    white = '\033[1m'
    under = '\033[4m'

def sizeof(num, suffix='B'):
    for unit in [' ','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return('{:>4} {}{}'.format(format(num, '.3g'), unit, suffix))
        num /= 1024.0

def rikues(alamat, leng):
    user_agent = {'User-agent': UserAgent().random}
    r = requests.get(str(alamat), headers = user_agent, timeout = 5, allow_redirects = False, verify = False)
    num = int(len(r.text))
    status = r.status_code
    if status == 200:
        if alamat == '': pass
        elif len(r.text) == leng: pass
        else: sys.stdout.write(cl.green + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
    elif status == 301:
        if len(r.text) == leng: pass
        else: sys.stdout.write(cl.red + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
    elif status == 500:
        if len(r.text) == leng: pass
        else: sys.stdout.write(cl.pink + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
    elif status == 401:
        if len(r.text) == leng: pass
        else: sys.stdout.write(cl.yellow + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
    elif status == 403:
        if ".ht" in alamat: pass
        elif len(r.text) == leng: pass
        else: sys.stdout.write(cl.blue + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),alamat) + cl.end)

def prog():
    sys.stdout.flush()
    sys.stdout.write('| {} | [+] Wait a moment ...\r'.format(datetime.now().strftime('%H:%M:%S')))
    sys.stdout.flush()
    sys.stdout.write('| {} | [x] Wait a moment ...\r'.format(datetime.now().strftime('%H:%M:%S')))

def scanner(url, wordlist):
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Fix insecure ssl
        resource.setrlimit(resource.RLIMIT_NOFILE, (8192, 8192)) # Fix to many open file (RAM => 8GB)
        user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        cek = requests.get(url, headers = user_agent, timeout = 5, verify = False)
        leng = len(cek.text)
        no = 0
        file = open(wordlist, 'r', encoding='ISO-8859-1').read().split('\n')
        lcount = sum(1 for line in open(wordlist, 'r', encoding='ISO-8859-1'))
        print('===============================================================================')
        print('| Time     | Info          | URL                                              |')
        print('===============================================================================')
        executor = ThreadPoolExecutor(max_workers=100)
        futures = []
        for line in file:
            try:
                target = str(url) + str(line)
                a = executor.submit(rikues, target, leng)
                futures.append(a)
                no = no + 1
                jumlah = ( no * 100 ) / lcount
                sys.stdout.flush()
                sys.stdout.write("| {} | {}% Line : {}\r".format(datetime.now().strftime('%H:%M:%S'), int(jumlah), int(no)))
                sys.stdout.flush()
            except(KeyboardInterrupt,SystemExit):
                print('\r| {} | Exiting program ...'.format(datetime.now().strftime('%H:%M:%S')))
                break

        while True:
            try:
                prog()
                cek = a.done()
                if cek == True:
                    sleep(3)
                    print('===============================================================================');
                    break

            except KeyboardInterrupt:
                print('\r| {} | Exiting program ...'.format(datetime.now().strftime('%H:%M:%S')))
                print('===============================================================================')
                break

    except:
        print('[!] Invalid address or target is down..')

def directory_scanner(url):
    scanner(url, 'dict/dirs.txt')

def directory_scanner_indo(url):
    scanner(url, 'dict/indonesia.txt')

def directory_scanner_english(url):
    scanner(url, 'dict/english.txt')