import os
from utils.logger import log_event

CRITICAL_PIDS = {0, 4}
SAFE_IPS = {"127.0.0.1", "::1"}

# Memory of already blocked IPs (runtime)
BLOCKED_IPS = set()

def heal(threat):
    t = threat.get("type")

    # -------- Process handling --------
    if t == "MALICIOUS_PROCESS":
        pid = threat.get("pid")

        if pid in CRITICAL_PIDS or pid is None:
            return

        os.system(f"taskkill /PID {pid} /F")
        log_event(f"Terminated process PID {pid}")

    # -------- Network handling --------
    elif t == "SUSPICIOUS_IP":
        ip = threat.get("ip")

        if ip is None or ip in SAFE_IPS:
            return

        # Prevent repeated blocking
        if ip in BLOCKED_IPS:
            return

        os.system(
            f'netsh advfirewall firewall add rule name="SHCS_Block_{ip}" '
            f'dir=in action=block remoteip={ip}'
        )

        BLOCKED_IPS.add(ip)
        log_event(f"Blocked IP {ip}")


