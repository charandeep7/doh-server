import socket
from doh_proxy.doh_client import query_doh

def start_dns_server(ip='0.0.0.0', port=53):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    sock.settimeout(1.0)
    print(f"[+] Listening on {ip}:{port}")

    try:
        while True:
            try:
                data, addr = sock.recvfrom(512)
                client_ip, _ = addr
                response = query_doh(data, client_ip)
                if response:
                    sock.sendto(response, addr)
            except socket.timeout:
                continue
            except Exception as e:
                print(f"[!] Server error: {e}")
    except KeyboardInterrupt:
        print("\n[✋] Shutting down proxy gracefully.")
    finally:
        sock.close()