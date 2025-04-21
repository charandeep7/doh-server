from collections import OrderedDict
import hashlib
import time

class LRUCacheWithTTL:
    def __init__(self, capacity=256, ttl=120):
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()  # key -> (value, timestamp)

    def _hash(self, query_bytes):
        return hashlib.sha256(query_bytes).hexdigest()

    def get(self, query_bytes):
        key = self._hash(query_bytes)
        entry = self.cache.get(key)

        if entry:
            value, timestamp = entry
            if time.time() - timestamp < self.ttl:
                self.cache.move_to_end(key)
                return value
            else:
                del self.cache[key]  # expired
        return None

    def set(self, query_bytes, response_bytes):
        key = self._hash(query_bytes)
        self.cache[key] = (response_bytes, time.time())
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)