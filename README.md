# NetScan Pro 🔍

A Python-based network security assessment tool built for penetration testing practice.

## Features
- 🔍 TCP Port Scanning
- 🎯 Banner Grabbing  
- ⚙️ Service Detection (FTP, SSH, SMB, HTTP, Telnet etc.)
- 📊 JSON Report Generation

## Requirements
- Python 3.x
- Kali Linux (recommended)

## Usage

Basic scan:
python3 scanner.py 192.168.220.129

Custom port range:
python3 scanner.py 192.168.220.129 -s 1 -e 500

Save JSON report:
python3 scanner.py 192.168.220.129 -r

## Sample Results
Tested on Metasploitable2 — Found 12 open ports:
- Port 21 | FTP | vsFTPd 2.3.4
- Port 22 | SSH | OpenSSH 4.7p1
- Port 80 | HTTP
- Port 445 | SMB
- Port 23 | Telnet

## Author
Krishan Sharma

## Disclaimer
For authorized and educational testing only.
