#!/usr/bin/env python3
# NetScan Pro - Security Assessment Tool
# Author: Krishan Sharma

import socket
import argparse
import json
import datetime
import sys

# ─── Banner ───────────────────────────
def banner():
    print("""
         NetScan Pro v1.0  
    """)

# ─── Port Scanner ─────────────────────
def scan_ports(target, start_port, end_port):
    print(f"\n[*] Scanning {target} : ports {start_port}-{end_port}\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"    [+] Port {port} OPEN")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass

    return open_ports

# ─── Banner Grabbing ───────────────────
def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return "No banner"

# ─── Service Guesser ──────────────────
def guess_service(port):
    common = {
        21: "FTP", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP",
        443: "HTTPS", 3306: "MySQL",
        8080: "HTTP-Alt", 445: "SMB"
    }
    return common.get(port, "Unknown")

# ─── Report Generator ─────────────────
def save_report(target, results):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/scan_{target}_{timestamp}.json"

    report = {
        "target": target,
        "scan_time": timestamp,
        "open_ports": results
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\n[+] Report saved: {filename}")

# ─── Main ─────────────────────────────
def main():
    banner()

    parser = argparse.ArgumentParser(description="NetScan Pro - Security Tool")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-r", "--report", action="store_true", help="Save JSON report")

    args = parser.parse_args()

    # Scan
    open_ports = scan_ports(args.target, args.start, args.end)

    # Banner grab + service guess
    results = []
    print("\n[*] Service Detection:\n")
    for port in open_ports:
        service = guess_service(port)
        b = grab_banner(args.target, port)
        print(f"    Port {port} | {service} | Banner: {b}")
        results.append({
            "port": port,
            "service": service,
            "banner": b
        })

    # Report save
    if args.report:
        save_report(args.target, results)

main()
