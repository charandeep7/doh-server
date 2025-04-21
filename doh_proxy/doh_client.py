import base64
import requests
from doh_proxy.config import UPSTREAM_DOH_URL
from doh_proxy.logger import log_query
from doh_proxy.cache import LRUCacheWithTTL

cache = LRUCacheWithTTL(capacity=256, ttl=120)

def query_doh(dns_query_bytes, client_ip):
    ttl = 120
    cached = cache.get(dns_query_bytes)
    if cached:
        log_query(client_ip, dns_query_bytes, cache_hit=True, ttl=ttl)
        return cached

    encoded = base64.urlsafe_b64encode(dns_query_bytes).rstrip(b'=').decode()
    headers = {"accept": "application/dns-message"}
    url = f"{UPSTREAM_DOH_URL}?dns={encoded}"

    try:
        response = requests.get(url, headers=headers, timeout=2)
        response.raise_for_status()
        result = response.content

        cache.set(dns_query_bytes, result)
        log_query(client_ip, dns_query_bytes, cache_hit=False, ttl=ttl)

        return result
    except requests.RequestException as e:
        print(f"[!] DoH request failed: {e}")
        return None