import socket

def scan_port(ip, port):
  try:
    sock = socket.socket()
    sock.connect((ip, port))
    print(f"[+] Port Opened: {port}")
  except:
    pass

def scan(target, ports):
  print(f"\nStarting Scan for {target}")
  for port in range (1, ports):
    scan_port(target, port)

targets = input("[*] Enter a target IPs to scan (split by ,): ")
ports = int(input("[*] Enter how many ports to scan: "))

if ',' in targets:
  print("[*] Scanning multiple targets")
  for ip_addr in targets.split(','):
    scan(ip_addr.strip(' '), ports)
else:
  scan(targets, ports)