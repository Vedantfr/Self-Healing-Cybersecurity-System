import psutil

BLACKLIST = ["xmrig", "miner", "hacktool"]
CRITICAL_PIDS = {0, 4}

def get_suspicious_processes():
    suspicious = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            pid = proc.info['pid']
            name = (proc.info['name'] or "").lower()
            cpu = proc.info['cpu_percent'] or 0

            if pid in CRITICAL_PIDS:
                continue

            if any(bad in name for bad in BLACKLIST):
                suspicious.append(proc.info)
            elif cpu > 80:
                suspicious.append(proc.info)

        except Exception:
            continue

    return suspicious

