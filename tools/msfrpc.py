#!/usr/bin/env python3
from metasploit.msfrpc import MsfRpcClient
import subprocess
import os

def msfrpc():
    try:
        if ':55553' not in subprocess.getoutput('netstat -ntlp'):
            os.system('msfrpcd -S -a 127.0.0.1 -P darksplitz -U msf')
        while True:
            run = subprocess.getoutput('netstat -ntlp')
            if ':55553' in run: break
        rat = MsfRpcClient('darksplitz', server='127.0.0.1', ssl=False)
        cmd = rat.consoles.console()
        baner = cmd.read()
        baner = baner['data']
        print(baner)
        while True:
            x = cmd.read()
            console = rat.consoles.list['consoles'][-1]['prompt']
            console = console.replace('\x01\x02', '')
            run = input('\r' + console)
            if run == '':
                x = cmd.read()
                continue
            if run == 'exit': break
            cmd.write(run)
            for i in range(0, 30):
                sh = cmd.read()
                sh = sh['data']
                if sh != '':
                    print(sh)
                    sh = cmd.read()
                    break
    except KeyboardInterrupt:
        print('\r[!] Exiting program...')
        exit()
    except:
        print('\r[!] Cannot connect to msfrpc service...')
