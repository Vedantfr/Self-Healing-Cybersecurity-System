import subprocess
import psutil

AGENT_EXE = r"C:\MajorProject\shcs\dist\main.exe"
AGENT_NAME = "main.exe"


def is_agent_running():
    for p in psutil.process_iter(["name"]):
        if p.info["name"] == AGENT_NAME:
            return True
    return False


def start_agent():
    if not is_agent_running():
        subprocess.Popen(
            [AGENT_EXE, "--agent"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )


def stop_agent():
    for p in psutil.process_iter(["name"]):
        if p.info["name"] == AGENT_NAME:
            p.kill()
