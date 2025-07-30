import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            print(f"[+] Port {port} açık!")
    except (socket.timeout, ConnectionRefusedError):
        pass

def port_scanner(ip, start_port=1, end_port=1024):
    print(f"Port taraması başlatıldı: {ip}")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    target_ip = input("Hedef IP adresini girin: ")
    start_port = int(input("Başlangıç portu (varsayılan: 1): ") or 1)
    end_port = int(input("Bitiş portu (varsayılan: 1024): ") or 1024)
    port_scanner(target_ip, start_port, end_port)
