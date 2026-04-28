# NetScan Pro 🔍

A Python-based network security assessment tool built for penetration testing practice.

## 🛠️ Features
- TCP Port Scanning
- Banner Grabbing
- Service Detection (FTP, SSH, SMB, HTTP, Telnet)
- JSON Report Generation

## 💻 Requirements
- Python 3.x
- Kali Linux (recommended)

## 🚀 Usage

Basic scan:
Custom port range:
Save JSON report:


## 🎯 Real Lab Results (Metasploitable2)

Tested on Metasploitable2 in isolated VirtualBox home lab.
Found 12 open ports:

| Port | Service | Banner |
|------|---------|--------|
| 21 | FTP | vsFTPd 2.3.4 |
| 22 | SSH | OpenSSH 4.7p1 |
| 23 | Telnet | - |
| 25 | SMTP | Postfix Ubuntu |
| 53 | DNS | - |
| 80 | HTTP | - |
| 111 | RPC | - |
| 139 | NetBIOS | - |
| 445 | SMB | - |
| 512 | Rexec | - |
| 513 | Rlogin | - |
| 514 | Rsh | - |

## 📁 Project Structure

## 🔧 How It Works
1. Takes target IP as input
2. Scans specified port range using TCP sockets
3. Grabs service banners
4. Identifies running services
5. Saves results as JSON report

## 👨‍💻 Author
**Krishan Sharma**
Penetration Tester | Bug Hunter
- GitHub: github.com/wptechguard-glitch
- LinkedIn: linkedin.com/in/krishan-sharma-254aba304

## ⚠️ Disclaimer
This tool is for authorized and educational testing only.
Do not use against systems without permission.