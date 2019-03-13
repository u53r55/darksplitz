#!/usr/bin/env python3
from re import search
import requests
import json
import random

def md5crack(hash):
    if len(hash) == 32: pass
    else:
        print('[!] Hash invalid...')
        return False

    requests.packages.urllib3.disable_warnings()
    user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    print('[*] Cracking from nitrxgen')
    try: req = requests.get('http://www.nitrxgen.net/md5db/' + hash, headers = user_agent, timeout = 5).text
    except: req = 'onyon'
    if req != '':
        print('[+] Found : ' + req)
    else:
        print('[*] Cracking from hashtoolkit')
        try: req = requests.get('http://hashtoolkit.com/reverse-hash?hash=' + hash, headers = user_agent, timeout = 5).text
        except: req = 'onyon'
        if 'Hashes for:' in req:
            pasw = search('Hashes for: <code>(.*?)</code>', req).group(1)
            print('[+] Found : ' + pasw)
        else:
            print('[*] Cracking from gromweb')
            try: req = requests.get('https://md5.gromweb.com/?md5=' + hash, headers = user_agent, timeout = 5).text
            except: req = 'onyon'
            if 'was succesfully' in req:
                pasw = search('<em class="long-content string">(.*?)</em></p>', req).group(1)
                print('[+] Found : ' + pasw)
            else:
                print('[*] Cracking from my-addr')
                x = random.choice(range(0, 30))
                y = random.choice(range(0, 30))
                data = {'md5': hash, 'x': x, 'y': y}
                try: req = requests.post('http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', data = data, headers = user_agent, timeout = 5).text
                except: req = 'onyon'
                if 'Hashed string' in req:
                    pasw = search('Hashed string</span>: (.*?)</div>', req).group(1)
                    print('[+] Found : ' + pasw)
                else:
                    print('[+] Hash not found...')
