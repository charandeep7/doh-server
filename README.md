# 🔐 DNS-over-HTTPS Proxy (Python)

A lightweight DNS-over-HTTPS (DoH) proxy written in Python that:
- Accepts DNS queries over UDP
- Forwards them securely to a DoH server (e.g., Cloudflare)
- Responds with encrypted DNS results
- Caches results with TTL (120s)
- Logs each query to file and SQLite

---

## ✨ Features

- 🔒 Secure DNS resolution using HTTPS (RFC 8484)
- ⚡ UDP Server on Port 53 (acts like a real DNS resolver)
- 🧠 In-memory LRU Cache with TTL (default: 120s)
- 🗃 Persistent logging via SQLite + plaintext logs
- 🧾 Graceful shutdown with keyboard interrupt support
- 💾 Lightweight: Python 3 only, no extra dependencies beyond `requests`

---