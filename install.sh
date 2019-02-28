#!/usr/bin/env bash

if [[ "$UID" != "0" ]]; then
  echo "This script must be run as root !!!"
  exit
fi
apt-get -y install masscan libffi-dev python3-dev python3-pip libssl-dev host nmap
pip3 install requests
pip3 install PySquashfsImage
pip3 install ropper
pip3 install fake_useragent
pip3 install netaddr
pip3 install scapy
pip3 install netifaces
pip3 install psutil
pip3 install --upgrade pip
python3 -c "import metasploit.msfrpc" 2&> /dev/null
if [[ "$?" != "0" ]]; then
  git clone https://github.com/koboi137/pymetasploit
  cd pymetasploit
  python3 setup.py install
  cd ..
  rm -rf pymetasploit
fi
