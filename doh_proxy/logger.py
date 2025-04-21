from datetime import datetime
from doh_proxy.db import log_to_db

log_file = "logs/queries.log"

def log_query(client_ip, query_bytes, cache_hit, ttl):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    domain = extract_domain(query_bytes)
    log_line = f"[{timestamp}] {client_ip} queried {domain} (Cache: {'Yes' if cache_hit else 'No'}) TTL: {ttl}s"

    print(log_line)
    with open(log_file, "a") as f:
        f.write(log_line + "\n")

    log_to_db(timestamp, client_ip, domain, cache_hit, ttl)

def extract_domain(query_bytes):
    try:
        qname = []
        i = 12
        while True:
            length = query_bytes[i]
            if length == 0:
                break
            qname.append(query_bytes[i+1:i+1+length].decode())
            i += length + 1
        return '.'.join(qname)
    except:
        return "<unknown>"