#!/usr/bin/env python3
import requests, json, os, sys, random

def prog():
    data = ('+', 'x')
    resp = random.choice(data)
    sys.stdout.flush()
    sys.stdout.write('[{}] Collecting ...\r'.format(resp))

def wayback(domain):
    try:
        if domain == '' or '.' not in domain:
            print('[!] exe : wayback www.example.com')
            return False
        pwd = os.getcwd()
        url = 'https://web.archive.org/cdx/search?url={}&matchType=prefix&output=json&fl=original'.format(domain)
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
        print('[*] Collecting url ...')
        r = requests.get(url, headers = header)
        content = r.text
        data = json.loads(content)
        urls = []
        print('[*] Saving url into file ...')
        for yurl in data:
            yur = yurl[0]
            if yur not in urls:
                prog()
                urls.append(yur)
                open(domain + '.txt', 'a').write('{}\n'.format(yur))
            else: pass
        print('[+] Saved to {}/{}.txt'.format(pwd, domain))
    except KeyboardInterrupt:
        print('\r[!] Saved to {}{}.txt'.format(pwd, domain))
        exit()