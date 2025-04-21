from doh_proxy.server import start_dns_server
from doh_proxy.config import LISTEN_IP, LISTEN_PORT
from doh_proxy.db import init_db

if __name__ == "__main__":
    init_db()
    start_dns_server(LISTEN_IP, LISTEN_PORT)