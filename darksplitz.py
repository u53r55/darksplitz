#!/usr/bin/env python3
#########################################################
# Shellscript : darksplitz.py - Dark Splitz
# Author      : koboi137
# Category    : Penetration testing framework
#
# Copyright © 2018 - 2019 Backbox Indonesia
#########################################################

from cmd import Cmd
import subprocess
import os

modul = '''
 Module
 ======

     Tools                   Description
     -----                   -----------
     extract_credential      Extract mikrotik credential (user.dat)
     password_generator      Password generator
     reverse_ip              Reverse IP lookup
     arpsniff                Mac address sniffer
     md5crack                Online md5 cracker
     maclookup               Mac address lookup
     maclookup_mass          Mass mac address lookup
     wayback                 Collecting url from web.archive.org

     Exploit                 Description
     -------                 -----------
     winbox_exploit_ip       Winbox exploit (CVE-2018-14847)
     winbox_exploit_mac      Winbox exploit (CVE-2018-14847)
     winbox_exploit_mass     Mass winbox exploit (CVE-2018-14847)
     chimeyred_mipsbe        ChimeyRed exploit for mipsbe (Mikrotik)
     webapps_exploit         Exploit web application
     appledos                Mass apple dos (CVE-2018-4407)
     libssh                  Libssh exploit (CVE-2018-10933)

     Scanner                 Description
     -------                 -----------
     mac_discover            Discovering Mikrotik device (MAC Server)
     dirscan                 Directory scanner (global wordlist)
     dirscan_id              Directory scanner (indonesian wordlist)
     dirscan_en              Directory scanner (english wordlist)
     subdomain_scanner       Subdomain scanner (global wordlist)
     subdomain_scanner_id    Subdomain scanner (indonesian wordlist)
     subdomain_scanner_en    Subdomain scanner (english wordlist)
     arpscan                 Mac address scanner
     arpscan_nmap            Mac address scanner (nmap)
     arpping                 Mac address pinger
     vhost_scanner           Vhost scanner (bypass cloudflare)
     wpslug                  Mass bruteforce (wordpress)
     wpslug_file             Mass bruteforce (wordpress)
'''

class MyPrompt(Cmd):
    def emptyline(self):
        pass

    def default(self, argv):
        os.system(argv)

    def do_module(self, args):
        print(modul)

    def do_msfrpc(self, args):
        from tools.msfrpc import msfrpc
        msfrpc()

    # Tools
    def do_reverse_ip(self, args):
        """[+] Reverse IP lookup\n[!] exe : reverse_ip 1.1.1.1"""
        from tools.reverseip import reverse_ip
        reverse_ip(args)

    def do_password_generator(self, args):
        """[+] Password generator"""
        from tools.passgen import password_generator
        password_generator()

    def do_extract_credential(self, args):
        """[+] Extract mikrotik credential (user.dat)\n[!] exe : extract_credential /tmp/user.dat"""
        from tools.extract_user import extract_credential
        extract_credential(args)

    def do_arpsniff(self, args):
        """[+] Mac address sniffer"""
        from tools.arpsniff import arpsniff
        arpsniff()

    def do_md5crack(self, args):
        """[+] Online md5 cracker\n[!] exe : md5crack 21232f297a57a5a743894a0e4a801fc3"""
        from tools.md5crack import md5crack
        md5crack(args)

    def do_maclookup(self, args):
        """[+] Mac address lookup\n[!] exe : maclookup 64:d1:54:ff:ff:ff"""
        from tools.maclookup import checker
        checker(args)

    def do_maclookup_mass(self, args):
        """[+] Mass mac address lookup\n[!] exe : maclookup_mass /tmp/mac.txt"""
        from tools.maclookup import filecheck
        filecheck(args)

    def do_wayback(self, args):
        """[+] Collecting url from web.archive.org\n[!] exe : wayback www.example.com"""
        from tools.wayback import wayback
        wayback(args)

    def do_drkshell(self, args):
        """[+] Php web backdoor (Dark Shell)\n[!] exe : drkshell http://127.0.0.1/shell.php"""
        from tools.drkshell import drkshell
        drkshell(args)

    # Exploit
    def do_winbox_exploit_ip(self, args):
        """[+] Winbox exploit (CVE-2018-14847)\n[!] exe : winbox_exploit_ip 127.0.0.1"""
        from exploit.WinboxExploitIP import winbox_exploit_ip
        winbox_exploit_ip(args)

    def do_winbox_exploit_mac(self, args):
        """[+] Winbox exploit (CVE-2018-14847)\n[!] exe : winbox_exploit_mac 64:d1:54:ff:ff:ff"""
        from exploit.WinboxExploitMAC import winbox_exploit_mac
        winbox_exploit_mac(args)

    def do_winbox_exploit_mass(self, args):
        """[+] Mass winbox exploit (CVE-2018-14847)\n[!] exe : winbox_exploit_mass 127.0.0.1/24"""
        from exploit.WinboxExploitMass import winbox_exploit_mass
        winbox_exploit_mass(args)

    def do_chimeyred_mipsbe(self, args):
        """[+] ChimeyRed exploit for mipsbe\n[!] exe : chimeyred_mipsbe 127.0.0.1"""
        from exploit.chimeyred_mipsbe import chimeyred_mipsbe
        chimeyred_mipsbe(args)

    def do_webapps_exploit(self, args):
        """[+] Exploit web application\n[!] exe : webapps_exploit http://target.com/"""
        from exploit.webapps_exploit import webapps_exploit
        webapps_exploit(args)

    def do_appledos(self, args):
        """[+] Mass apple dos (CVE-2018-4407)\n[!] exe : appledos 127.0.0.0/24\n[!] exe : appledos 127.0.0.0/24 445"""
        from exploit.appledos import appledos
        try:
            rang = args.split(' ')[0]
            port = int(args.split(' ')[1])
            appledos(rang, port)
        except:
            try: appledos(args, 80)
            except: print('[!] Wrong input...')

    def do_libssh(self, args):
        """[+] Libssh exploit (CVE-2018-10933)\n[!] exe : libssh 127.0.0.1 2222"""
        from exploit.libssh import libssh
        try:
            ip = args.split(' ')[0]
            port = int(args.split(' ')[1])
            libssh(ip, port)
        except:
            try: libssh(ip, 22)
            except: print('[!] Wrong input...')

    # Scanner
    def do_mac_discover(self, args):
        """[+] Discovering Mikrotik device (MAC Server)"""
        from scanner.MACServerDiscover import mac_discover
        mac_discover()

    def do_dirscan(self, args):
        """[+] Directory scanner (global wordlist)\n[!] exe : dirscan http://target.com/"""
        from scanner.dirscan import directory_scanner
        directory_scanner(args)

    def do_dirscan_id(self, args):
        """[+] Directory scanner (indonesian wordlist)\n[!] exe : dirscan_id http://target.com/"""
        from scanner.dirscan import directory_scanner_indo
        directory_scanner_indo(args)

    def do_dirscan_en(self, args):
        """[+] Directory scanner (english wordlist)\n[!] exe : dirscan_en http://target.com/"""
        from scanner.dirscan import directory_scanner_english
        directory_scanner_english(args)

    def do_subdomain_scanner(self, args):
        """[+] Subdomain scanner (global wordlist)\n[!] exe : subdomain_scanner target.com"""
        from scanner.subscanner import subdomain_scanner
        subdomain_scanner(args)

    def do_subdomain_scanner_id(self, args):
        """[+] Subdomain scanner (indonesian wordlist)\n[!] exe : subdomain_scanner_id target.com"""
        from scanner.subscanner import subdomain_scanner_indo
        subdomain_scanner_indo(args)

    def do_subdomain_scanner_en(self, args):
        """[+] Subdomain scanner (english wordlist)\n[!] exe : subdomain_scanner_en target.com"""
        from scanner.subscanner import subdomain_scanner_english
        subdomain_scanner_english(args)

    def do_arpscan(self, args):
        """[+] Mac address scanner"""
        from scanner.arpscan import arpscan
        arpscan()

    def do_arpscan_nmap(self, args):
        """[+] Mac address scanner (nmap)\n[!] exe : arpscan_nmap"""
        from scanner.arpscanmap import arpscanmap
        arpscanmap()

    def do_arpping(self, args):
        """[+] Mac address pinger\n[!] exe : arpping 127.0.0.0/24"""
        from scanner.arpping import arpping
        arpping(args)

    def do_vhost_scanner(self, args):
        """[+] Vhost scanner (bypass cloudflare)\n[!] exe : vhost_scanner 127.0.0.0/24 http://target.com/"""
        from scanner.vhostscanner import vhost_scanner
        try:
            rang = args.split(' ')[0]
            url = args.split(' ')[1]
            vhost_scanner(rang, url)
        except:
            print('[!] Wrong input...')

    def do_wpslug(self, args):
        """[+] Mass bruteforce (wordpress)\n[!] exe : wpslug 1.1.1.1"""
        from scanner.wpslug import wpslug
        wpslug(args, False)

    def do_wpslug_file(self, args):
        """[+] Mass bruteforce (wordpress)\n[!] exe : wpslug_file /root/target.txt"""
        from scanner.wpslug import wpslug_file
        wpslug_file(args, False)

    def do_exit(self, args):
        print("[!] Exiting program...")
        raise SystemExit

def app():
    try:
        prompt = MyPrompt()
        prompt.prompt = '\r[?] darksplitz >> '
        prompt.cmdloop('')
    except KeyboardInterrupt:
        print("\r[!] Exiting program...")
        raise SystemExit

def main():
    try:
        cek = subprocess.getoutput('netstat -ntlp')
        if '127.0.0.1:55553' in cek: msfrpc = True
        else: msfrpc = False
        banner = " ____             _      ____        _ _ _\n"
        banner += "|  _ \  __ _ _ __| | __ / ___| _ __ | (_) |_ ____\n"
        banner += "| | | |/ _` | '__| |/ / \___ \| '_ \| | | __|_  /\n"
        banner += "| |_| | (_| | |  |   <   ___) | |_) | | | |_ / /\n"
        banner += "|____/ \__,_|_|  |_|\_\ |____/| .__/|_|_|\__/___|\n"
        banner += "                              |_|\n"
        banner += "        Frameworksploit\n"
        banner += "   Backbox Indonesia @ 2018 - 2019\n\n"
        banner += "[+] Msfrpc => {}".format(msfrpc)
        prompt = MyPrompt()
        prompt.prompt = '\r[?] darksplitz >> '
        prompt.cmdloop(banner)
    except KeyboardInterrupt:
        print("\r[!] Exiting program...")
        raise SystemExit

if __name__ == '__main__':
    main()
