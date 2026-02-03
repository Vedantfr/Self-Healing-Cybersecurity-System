import psutil

SAFE_IPS = {"127.0.0.1", "::1"}

# Known cloud / trusted ranges (basic)
TRUSTED_PREFIXES = (
    "13.", "15.", "20.", "40.", "52.",     # Microsoft / Azure
    "142.250.", "142.251.",               # Google
    "104.16.", "104.17.", "104.18.",      # Cloudflare
)

def is_private_ip(ip):
    return (
        ip.startswith("10.") or
        ip.startswith("192.168.") or
        ip.startswith("172.")
    )

def is_trusted_ip(ip):
    return ip.startswith(TRUSTED_PREFIXES)

def get_suspicious_connections():
    suspicious = []

    for conn in psutil.net_connections(kind="inet"):
        if not conn.raddr:
            continue

        ip = conn.raddr.ip

        if ip in SAFE_IPS:
            continue

        if is_private_ip(ip):
            continue

        if is_trusted_ip(ip):
            continue

        suspicious.append({
            "ip": ip,
            "pid": conn.pid
        })

    return suspicious

