#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║                  NETWORK OSINT & PORT SCANNER                       ║
║               Advanced IP Reconnaissance Tool v2.0                  ║
╚══════════════════════════════════════════════════════════════════════╝

Author:     xdrew87
License:    MIT
GitHub:     https://github.com/xdrew87/network-osint-scanner
Description: Advanced network reconnaissance tool combining OSINT and
            port scanning capabilities with real-time threat detection.

Features:
  • Real-time port scanning (1-65535)
  • Geolocation tracking
  • VPN/Proxy detection
  • ISP and ASN lookup
  • Threat level assessment
  • Multiple API cross-referencing
"""

import socket
import requests
import sys
import time
import json
from datetime import datetime
import os

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 8080, 8443]

# ANSI Color codes
class Colors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

def clear_screen():
	"""Clear terminal screen"""
	os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
	"""Print application banner with ASCII art"""
	print(f"{Colors.BOLD}{Colors.HEADER}")
	print("  ╔════════════════════════════════════════════════════════════════════╗")
	print("  ║                                                                    ║")
	print("  ║      ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ║")
	print("  ║      ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║  ║")
	print("  ║      ██╔██╗ ██║███████╗   ██║   ██║ █╗ ██║██║   ██║██████╔╝██║  ║")
	print("  ║      ██║╚██╗██║╚════██║   ██║   ██║███╗██║██║   ██║██╔══██╗╚═╝  ║")
	print("  ║      ██║ ╚████║███████║   ██║   ╚███╔███╝╚██████╔╝██║  ██║██╗   ║")
	print("  ║      ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ║")
	print("  ║                                                                    ║")
	print("  ║           Advanced IP Reconnaissance & Port Scanner Tool           ║")
	print("  ║                         Version 2.0                                ║")
	print("  ║                                                                    ║")
	print("  ║                       Developed by: xdrew87                        ║")
	print("  ║               https://github.com/xdrew87/network-osint-scanner     ║")
	print("  ║                                                                    ║")
	print("  ╚════════════════════════════════════════════════════════════════════╝")
	print(f"{Colors.END}\n")

def print_menu():
	"""Print main menu with ASCII borders"""
	print(f"{Colors.BOLD}{Colors.CYAN}╔{'═'*68}╗{Colors.END}")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END} {Colors.BOLD}{Colors.YELLOW}⚙ MAIN MENU{Colors.END}" + " "*54 + f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}")
	print(f"{Colors.BOLD}{Colors.CYAN}╠{'═'*68}╣{Colors.END}")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.GREEN}[1]{Colors.END} Full OSINT Scan (Geolocation + Port Scan)")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.GREEN}[2]{Colors.END} Port Scan Only (Custom Range)")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.GREEN}[3]{Colors.END} Quick OSINT (Common Ports)")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.GREEN}[4]{Colors.END} Batch Scan (Multiple IPs)")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.CYAN}[5]{Colors.END} Help & Documentation")
	print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.RED}[0]{Colors.END} Exit")
	print(f"{Colors.BOLD}{Colors.CYAN}╚{'═'*68}╝{Colors.END}\n")

def print_help():
	"""Print help and documentation"""
	clear_screen()
	print_banner()
	print(f"{Colors.BOLD}{Colors.CYAN}Help & Documentation{Colors.END}\n")
	print("USAGE:")
	print("  python main.py <ip_or_domain>\n")
	print("SCANNING MODES:")
	print("  1. Full OSINT Scan   - Complete reconnaissance with all data")
	print("  2. Port Scan Only    - Custom port range scanning")
	print("  3. Quick OSINT       - Fast scan with common ports")
	print("  4. Batch Scan        - Scan multiple targets\n")
	print("API KEYS (Optional):")
	print("  - IPQualityScore: https://ipqualityscore.com")
	print("  - VPNAPI.io:      https://vpnapi.io/\n")
	print("EXAMPLES:")
	print("  python main.py 8.8.8.8")
	print("  python main.py google.com")
	print("  python main.py cloudflare.com\n")
	input(f"{Colors.CYAN}Press ENTER to return to menu...{Colors.END}")

def scan_ports(ip, ports=COMMON_PORTS, timeout=1):
	open_ports = []
	total = len(ports)
	for idx, port in enumerate(ports, 1):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(timeout)
			result = sock.connect_ex((ip, port))
			if result == 0:
				open_ports.append(port)
				print(f"  {Colors.GREEN}✓{Colors.END} Port {port} is OPEN", flush=True)
			sock.close()
		except Exception:
			continue
		# Progress indicator
		progress = int((idx / total) * 100)
		print(f"\r  Scanning: {progress}% ({idx}/{total})", end="", flush=True)
	print(f"\r  Scanning: 100% ({total}/{total})      \n", flush=True)
	return open_ports

def get_ipinfo(ip):
	try:
		resp = requests.get(f"https://suicixde.com/api/geoip.php?ip={ip}", timeout=5)
		if resp.status_code == 200:
			return resp.json()
	except Exception:
		pass
	return {}

def get_ipqualityscore(ip, api_key=None):
	# Get your API key from https://ipqualityscore.com
	API_KEY = api_key or "YOUR_IPQUALITYSCORE_API_KEY"  # Replace with your API key
	try:
		resp = requests.get(f"https://ipqualityscore.com/api/json/ip/{API_KEY}/{ip}", timeout=5)
		if resp.status_code == 200:
			return resp.json()
	except Exception:
		pass
	return {}

# vpnapi.io detection
def get_vpnapiio(ip, api_key=None):
	# Get your API key from https://vpnapi.io/
	API_KEY = api_key or "YOUR_VPNAPIIO_API_KEY"  # Replace with your API key
	try:
		resp = requests.get(f"https://vpnapi.io/api/{ip}?key={API_KEY}", timeout=5)
		if resp.status_code == 200:
			return resp.json()
	except Exception:
		pass
	return {}

def osint_report(ip, port_range=None):
	print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.END}")
	print(f"{Colors.BOLD}{Colors.HEADER}[+] OSINT REPORT FOR {ip}{Colors.END}")
	print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.END}\n")
	
	print(f"{Colors.CYAN}[*] Gathering IP Information...{Colors.END}")
	ipinfo = get_ipinfo(ip)
	# Optionally, set your API keys here
	IPQS_API_KEY = "YOUR_IPQUALITYSCORE_API_KEY"  # <-- Replace with your key
	VPNAPIIO_API_KEY = "YOUR_VPNAPIIO_API_KEY"    # <-- Replace with your key
	ipqs = get_ipqualityscore(ip, IPQS_API_KEY)
	vpnapi = get_vpnapiio(ip, VPNAPIIO_API_KEY)

	if ipinfo:
		print(f"\n{Colors.BOLD}{Colors.BLUE}[GEO-IP DATA]{Colors.END}")
		print(f"  IP:                  {Colors.GREEN}{ipinfo.get('ip', ip)}{Colors.END}")
		print(f"  Hostname:            {ipinfo.get('hostname', 'N/A')}")
		print(f"  City:                {ipinfo.get('city', 'N/A')}")
		print(f"  Region:              {ipinfo.get('region', 'N/A')}")
		print(f"  Country:             {ipinfo.get('country_name', ipinfo.get('country', 'N/A'))}")
		print(f"  ISP:                 {ipinfo.get('isp', 'N/A')}")
		print(f"  Organization:        {ipinfo.get('org', 'N/A')}")
		print(f"  ASN:                 {ipinfo.get('asn', ipinfo.get('asn_number', 'N/A'))}")
		print(f"  Connection Type:     {ipinfo.get('connection_type', 'N/A')}")
		print(f"  Threat Level:        {Colors.RED}{ipinfo.get('threat_level', 'N/A')}{Colors.END}")
		
		is_vpn = ipinfo.get('is_vpn', False)
		is_proxy = ipinfo.get('is_proxy', False)
		is_hosting = ipinfo.get('is_hosting', False)
		is_home_proxy = ipinfo.get('is_home_proxy', False)
		
		print(f"\n{Colors.BOLD}{Colors.BLUE}[SECURITY FLAGS]{Colors.END}")
		print(f"  VPN Detected:        {Colors.RED if is_vpn else Colors.GREEN}{'YES' if is_vpn else 'NO'}{Colors.END}")
		print(f"  Proxy Detected:      {Colors.RED if is_proxy else Colors.GREEN}{'YES' if is_proxy else 'NO'}{Colors.END}")
		print(f"  Hosting Provider:    {Colors.RED if is_hosting else Colors.GREEN}{'YES' if is_hosting else 'NO'}{Colors.END}")
		print(f"  Home Proxy:          {Colors.RED if is_home_proxy else Colors.GREEN}{'YES' if is_home_proxy else 'NO'}{Colors.END}")
		print(f"  Premium Data:        {Colors.YELLOW}{'YES' if ipinfo.get('premium', False) else 'NO'}{Colors.END}")
	else:
		print(f"{Colors.RED}[!] Could not retrieve geoip data.{Colors.END}")

	# Optionally, you can still show results from other APIs for cross-checking
	if ipqs or vpnapi:
		# IPQualityScore
		vpn_proxy_qs = ipqs.get('vpn', False) or ipqs.get('proxy', False) if ipqs else False
		hosting_qs = ipqs.get('hosting', False) if ipqs else False
		public_wifi_qs = ipqs.get('tor', False) or ipqs.get('active_vpn', False) if ipqs else False
		# vpnapi.io
		vpnapi_security = vpnapi.get('security', {}) if vpnapi else {}
		vpn_proxy_va = vpnapi_security.get('vpn', False) or vpnapi_security.get('proxy', False)
		hosting_va = vpnapi_security.get('hosting', False)
		public_wifi_va = vpnapi_security.get('tor', False) or vpnapi_security.get('relay', False)

		# Final verdict: True if either API says True
		vpn_proxy = vpn_proxy_qs or vpn_proxy_va
		hosting = hosting_qs or hosting_va
		public_wifi = public_wifi_qs or public_wifi_va

		print(f"\n{Colors.BOLD}{Colors.BLUE}[CROSS-CHECK - OTHER APIs]{Colors.END}")
		print(f"  VPN/Proxy:           {Colors.RED if vpn_proxy else Colors.GREEN}{'YES' if vpn_proxy else 'NO'}{Colors.END}")
		print(f"  Hosting:             {Colors.RED if hosting else Colors.GREEN}{'YES' if hosting else 'NO'}{Colors.END}")
		print(f"  Public WiFi/Hotspot: {Colors.RED if public_wifi else Colors.GREEN}{'YES' if public_wifi else 'NO'}{Colors.END}")
		if ipqs:
			print(f"  Fraud Score (IPQS):  {Colors.YELLOW}{ipqs.get('fraud_score', 'N/A')}{Colors.END}")
		if vpnapi:
			print(f"  VPNAPI Score:        {Colors.YELLOW}{vpnapi.get('score', 'N/A')}{Colors.END}")

	print(f"\n{Colors.CYAN}[*] Scanning Ports...{Colors.END}")
	print(f"{Colors.BOLD}{Colors.BLUE}[PORT SCAN RESULTS]{Colors.END}")
	if port_range:
		open_ports = scan_ports(ip, port_range)
	else:
		open_ports = scan_ports(ip)
	
	if open_ports:
		print(f"  {Colors.GREEN}✓ Open Ports Found: {', '.join(str(p) for p in open_ports)}{Colors.END}")
	else:
		print(f"  {Colors.YELLOW}○ No open ports found or host unreachable.{Colors.END}")
	
	print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.END}\n")
	
	# Save report to file
	save_report(ip, ipinfo, open_ports)

def save_report(ip, ipinfo, open_ports):
	"""Save scan report to file"""
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"report_{ip}_{timestamp}.txt"
	
	try:
		with open(filename, 'w') as f:
			f.write("="*70 + "\n")
			f.write(f"OSINT REPORT FOR {ip}\n")
			f.write("="*70 + "\n\n")
			f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
			
			if ipinfo:
				f.write("GEO-IP DATA:\n")
				f.write("-"*70 + "\n")
				f.write(f"IP:                  {ipinfo.get('ip', ip)}\n")
				f.write(f"Hostname:            {ipinfo.get('hostname', 'N/A')}\n")
				f.write(f"City:                {ipinfo.get('city', 'N/A')}\n")
				f.write(f"Region:              {ipinfo.get('region', 'N/A')}\n")
				f.write(f"Country:             {ipinfo.get('country_name', ipinfo.get('country', 'N/A'))}\n")
				f.write(f"ISP:                 {ipinfo.get('isp', 'N/A')}\n")
				f.write(f"Organization:        {ipinfo.get('org', 'N/A')}\n")
				f.write(f"ASN:                 {ipinfo.get('asn', ipinfo.get('asn_number', 'N/A'))}\n")
				f.write(f"Connection Type:     {ipinfo.get('connection_type', 'N/A')}\n")
				f.write(f"Threat Level:        {ipinfo.get('threat_level', 'N/A')}\n\n")
				
				f.write("SECURITY FLAGS:\n")
				f.write("-"*70 + "\n")
				f.write(f"VPN Detected:        {ipinfo.get('is_vpn', False)}\n")
				f.write(f"Proxy Detected:      {ipinfo.get('is_proxy', False)}\n")
				f.write(f"Hosting Provider:    {ipinfo.get('is_hosting', False)}\n")
				f.write(f"Home Proxy:          {ipinfo.get('is_home_proxy', False)}\n")
				f.write(f"Premium Data:        {ipinfo.get('premium', False)}\n\n")
			
			f.write("PORT SCAN RESULTS:\n")
			f.write("-"*70 + "\n")
			if open_ports:
				f.write(f"Open Ports: {', '.join(str(p) for p in open_ports)}\n")
			else:
				f.write("No open ports found.\n")
		
		print(f"{Colors.GREEN}[✓] Report saved as: {filename}{Colors.END}\n")
	except Exception as e:
		print(f"{Colors.RED}[!] Could not save report: {str(e)}{Colors.END}\n")

def interactive_mode():
	"""Interactive menu mode"""
	while True:
		clear_screen()
		print_banner()
		print_menu()
		
		choice = input(f"{Colors.CYAN}Select an option (0-5): {Colors.END}").strip()
		
		if choice == '0':
			print(f"\n{Colors.GREEN}Thanks for using Network OSINT Scanner!{Colors.END}")
			print(f"{Colors.CYAN}Developed by: xdrew87{Colors.END}\n")
			sys.exit(0)
		elif choice == '1':
			clear_screen()
			print_banner()
			target = input(f"{Colors.CYAN}Enter IP or domain: {Colors.END}").strip()
			try:
				ip = socket.gethostbyname(target)
				print(f"{Colors.GREEN}[✓] Resolved to: {ip}{Colors.END}")
				
				start_port = int(input(f"{Colors.CYAN}Enter start of port range: {Colors.END}"))
				end_port = int(input(f"{Colors.CYAN}Enter end of port range: {Colors.END}"))
				
				if start_port < 1 or end_port > 65535 or start_port > end_port:
					print(f"{Colors.RED}[!] Invalid port range.{Colors.END}")
					input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
					continue
				
				port_range = list(range(start_port, end_port + 1))
				osint_report(ip, port_range)
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
			except Exception as e:
				print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
		
		elif choice == '2':
			clear_screen()
			print_banner()
			target = input(f"{Colors.CYAN}Enter IP or domain: {Colors.END}").strip()
			try:
				ip = socket.gethostbyname(target)
				print(f"{Colors.GREEN}[✓] Resolved to: {ip}{Colors.END}\n")
				
				start_port = int(input(f"{Colors.CYAN}Enter start of port range: {Colors.END}"))
				end_port = int(input(f"{Colors.CYAN}Enter end of port range: {Colors.END}"))
				
				if start_port < 1 or end_port > 65535 or start_port > end_port:
					print(f"{Colors.RED}[!] Invalid port range.{Colors.END}")
					input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
					continue
				
				port_range = list(range(start_port, end_port + 1))
				print(f"\n{Colors.CYAN}[*] Starting port scan...{Colors.END}\n")
				open_ports = scan_ports(ip, port_range)
				
				print(f"\n{Colors.BOLD}{Colors.BLUE}[RESULTS]{Colors.END}")
				if open_ports:
					print(f"  {Colors.GREEN}✓ Open Ports: {', '.join(str(p) for p in open_ports)}{Colors.END}")
				else:
					print(f"  {Colors.YELLOW}No open ports found.{Colors.END}")
				
				input(f"\n{Colors.CYAN}Press ENTER to continue...{Colors.END}")
			except Exception as e:
				print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
		
		elif choice == '3':
			clear_screen()
			print_banner()
			target = input(f"{Colors.CYAN}Enter IP or domain: {Colors.END}").strip()
			try:
				ip = socket.gethostbyname(target)
				print(f"{Colors.GREEN}[✓] Resolved to: {ip}{Colors.END}\n")
				osint_report(ip)
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
			except Exception as e:
				print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
		
		elif choice == '4':
			clear_screen()
			print_banner()
			print(f"{Colors.CYAN}[*] Batch Scan Mode{Colors.END}\n")
			batch_file = input(f"{Colors.CYAN}Enter file with IPs (one per line): {Colors.END}").strip()
			try:
				with open(batch_file, 'r') as f:
					ips = [line.strip() for line in f if line.strip()]
				
				for target in ips:
					try:
						ip = socket.gethostbyname(target)
						print(f"{Colors.GREEN}Scanning: {ip}{Colors.END}")
						osint_report(ip)
					except Exception as e:
						print(f"{Colors.RED}[!] Could not resolve {target}: {str(e)}{Colors.END}\n")
				
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
			except Exception as e:
				print(f"{Colors.RED}[!] Error reading file: {str(e)}{Colors.END}")
				input(f"{Colors.CYAN}Press ENTER to continue...{Colors.END}")
		
		elif choice == '5':
			print_help()
			clear_screen()
		
		else:
			print(f"{Colors.RED}Invalid option. Please select 0-5.{Colors.END}")
			time.sleep(1)

if __name__ == "__main__":
	clear_screen()
	
	if len(sys.argv) > 1:
		# Command line mode
		print_banner()
		target = sys.argv[1]
		print(f"{Colors.CYAN}[*] Resolving target: {target}{Colors.END}")
		
		try:
			ip = socket.gethostbyname(target)
			print(f"{Colors.GREEN}[✓] Resolved to: {ip}{Colors.END}\n")
		except Exception:
			print(f"{Colors.RED}[!] Could not resolve {target}{Colors.END}")
			sys.exit(1)
		
		# Ask user for port range
		try:
			print(f"{Colors.CYAN}[*] Port Range Configuration:{Colors.END}")
			start_port = int(input(f"  {Colors.BOLD}Enter start of port range:{Colors.END} "))
			end_port = int(input(f"  {Colors.BOLD}Enter end of port range:{Colors.END} "))
			
			# Validate port range
			if start_port < 1 or end_port > 65535 or start_port > end_port:
				print(f"{Colors.RED}[!] Invalid port range. Please use ports between 1 and 65535 with start <= end.{Colors.END}")
				sys.exit(1)
			
			port_range = list(range(start_port, end_port + 1))
			print(f"{Colors.GREEN}[✓] Port range set: {start_port} - {end_port} ({len(port_range)} ports){Colors.END}\n")
		except ValueError:
			print(f"{Colors.RED}[!] Invalid input. Please enter valid port numbers.{Colors.END}")
			sys.exit(1)
		
		osint_report(ip, port_range)
	else:
		# Interactive mode
		interactive_mode()
