def analyze(data):
    threats = []

    system = data.get("system", {})
    if system.get("cpu", 0) > 90:
        threats.append({"type": "high_cpu"})

    processes = data.get("processes", [])
    for proc in processes:
        threats.append({
            "type": "suspicious_process",
            "pid": proc.get("pid")
        })

    network = data.get("network", [])
    for conn in network:
        threats.append({
            "type": "suspicious_connection",
            "ip": conn.get("ip")
        })

    return threats

