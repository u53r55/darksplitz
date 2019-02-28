#!/usr/bin/env python3
import requests
import json
import socket
import re

def reverse_ip(host, verbose=True):
    try:
        socket.inet_aton(host)
    except:
        print('[!] Invalid address')
        return False

    rev = []
    user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    data = {'remoteAddress': host, 'key': ''}
    try:
        print('[*] Get domain from yougetsignal')
        r = requests.post('https://domains.yougetsignal.com/domains.php', data = data, headers = user_agent, timeout = 5)
        get = json.loads(r.text)
        domlist = get['domainArray']
        for domain in domlist:
            if domain not in rev:
                rev.append(domain[0])

    except KeyboardInterrupt: print('\r[-] yougetsignal skiped')
    except: pass

    try:
        print('[*] Get domain from hackertarget')
        ht = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + host, headers = user_agent, timeout = 5)
        getht = ht.text
        for domain in getht.split('\n'):
            if domain == '': pass
            elif domain not in rev:
                rev.append(domain)
            else: pass

    except KeyboardInterrupt: print('\r[-] hackertarget skiped')
    except: pass

    try:
        print('[*] Get domain from viewdns')
        vd = requests.get('https://viewdns.info/reverseip/?host=' + host + '&t=1', headers = user_agent, timeout = 5)
        patern = re.compile('<tr> <td>(.+?)</td><td align="center">')
        form = re.findall(patern, vd.text)
        for ex in form:
            if ex not in rev:
                rev.append(ex)

    except KeyboardInterrupt: print('\r[-] viewdns skiped')
    except: pass

    try:
        print('[*] Get domain from domaineye')
        de = requests.get('https://domaineye.com/reverse-ip/' + host, headers = user_agent, timeout = 5)
        patern = re.compile("<a href = 'https://domaineye.com/similar/(.+?)'>")
        form = re.findall(patern, de.text)
        for eye in form:
            if eye not in rev:
                rev.append(eye)

    except KeyboardInterrupt: print('\r[-] domaineye skiped')
    except: pass

    if verbose == True:
        if len(rev) > 1:
            print('[+] ----------------------------')
            for hasil in rev:
                print('[+] ' + hasil)
            print('[+] ----------------------------')
            print('[!] Total : {} domain collected'.format(int(len(rev))))
        else: print('[-] Result not found')
    else:
        wpslug = []
        for hasil in rev:
            wpslug.append(hasil)
        return wpslug
