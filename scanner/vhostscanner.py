#!/usr/bin/env python3
from re import search
import requests
import ipaddress
import os
import sys

def vhost_scanner(reng, url):
    if os.getuid() != 0:
        print('[!] Need to run as root')
        return False
    try: net = ipaddress.IPv4Network(reng)
    except:
        print('[!] Range invalid...')
        return False
    try: asle = requests.get(url, timeout = 5).text
    except:
        print('[!] Target is down')
        return False
    asli = search('<title>(.*?)</title>', asle).group(1)
    os.rename('/etc/hosts', '/tmp/hosts')
    domain = url.split('://')[1]
    domain = domain.split('/')[0]
    for ip in net:
        sys.stdout.flush()
        sys.stdout.write('[+] Scanning {}\r'.format(ip))
        open('/etc/hosts', 'w').write(str(ip) + '\t' + domain)
        try:
            test = requests.get(url, timeout = 5).text
            teet = search('<title>(.*?)</title>', test).group(1)
            if asli == teet:
                print('\n[+] Real ip is : ' + str(ip))
                break
        except KeyboardInterrupt:
            print('\r[!] Exiting program...')
            break
        except: pass
    os.remove('/etc/hosts')
    os.rename('/tmp/hosts', '/etc/hosts')