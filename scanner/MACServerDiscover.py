#!/usr/bin/env python3
import socket, binascii, threading, time
# MAC server discovery by BigNerd95

search = True
devices = []

def discovery(sock):
    global search
    while search:
        sock.sendto(b"\x00\x00\x00\x00", ("255.255.255.255", 5678))
        time.sleep(1)

def mac_discover():
    global search
    global devices
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 5678))
    threading.Thread(target=discovery, args=(sock,)).start()
    print("[!] Looking for Mikrotik devices (MAC servers)")
    while search:
        try:
            data, addr = sock.recvfrom(1024)
            if b"\x00\x01\x00\x06" in data:
                start = data.index(b"\x00\x01\x00\x06") + 4
                mac = data[start:start+6]
                if mac not in devices:
                    devices.append(mac)
                    print('[+] ' + ':'.join('%02x' % b for b in mac))

        except KeyboardInterrupt:
            search = False
            print('\r[!] Scanning stoped...')
            break