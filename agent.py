<<<<<<< HEAD
import time
import traceback

from monitor import system_monitor
from monitor import process_monitor
from monitor import network_monitor
from detection import rule_engine
from response import self_heal
from utils.logger import log_event


def start_agent(stop_event=None):
    try:
        log_event("Agent entry reached")
        time.sleep(2)
        log_event("Agent initialized, entering main loop")

        while True:
            if stop_event is not None and stop_event.is_set():
                log_event("Agent stopping gracefully")
                break

            try:
                # 1️⃣ Collect data
                system_data = system_monitor.get_system_metrics()
                process_data = process_monitor.get_suspicious_processes()
                network_data = network_monitor.get_suspicious_connections()

                data = {
                    "system": system_data,
                    "processes": process_data,
                    "network": network_data,
                }

                # 2️⃣ HEARTBEAT (ALWAYS)
                log_event("Heartbeat: Monitoring active")

                # 3️⃣ Optional lightweight visibility (VERY useful in demo)
                log_event(
                    f"Snapshot | net={len(network_data)} "
                    f"proc={len(process_data)}"
                )

                # 4️⃣ Analyze threats (FAIL-SAFE)
                threats = rule_engine.analyze(data) or []

                # 5️⃣ Respond
                if threats:
                    for threat in threats:
                        log_event(f"Threat detected: {threat}")
                        self_heal.heal(threat)
                else:
                    log_event("No threats detected")

            except Exception as e:
                log_event(f"Runtime error: {e}")
                log_event(traceback.format_exc())

            # ⏱ Faster loop for demo visibility
            time.sleep(5)

    except Exception as e:
        log_event("FATAL AGENT ERROR")
        log_event(str(e))
        log_event(traceback.format_exc())
=======
import time
import traceback

from monitor import system_monitor
from monitor import process_monitor
from monitor import network_monitor
from detection import rule_engine
from response import self_heal
from utils.logger import log_event


def start_agent(stop_event=None):
    try:
        log_event("Agent entry reached")
        time.sleep(5)
        log_event("Agent initialized, entering main loop")

        while True:
            if stop_event is not None and stop_event.is_set():
                log_event("Agent stopping")
                break

            try:
                data = {
                    "system": system_monitor.get_system_metrics(),
                    "processes": process_monitor.get_suspicious_processes(),
                    "network": network_monitor.get_suspicious_connections()
                }

                threats = rule_engine.analyze(data)

                if threats:
                    for threat in threats:
                        self_heal.heal(threat)
                else:
                    log_event("Heartbeat: Agent running, no threats detected")

            except Exception as e:
                log_event(f"Runtime error: {e}")
                log_event(traceback.format_exc())

            time.sleep(10)

    except Exception as e:
        log_event("FATAL AGENT ERROR")
        log_event(str(e))
        log_event(traceback.format_exc())

>>>>>>> ff48c825f9fd64ae919885467895d38972d81c36
