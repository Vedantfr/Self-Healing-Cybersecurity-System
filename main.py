import sys
import os
import msvcrt

# ---------- Single instance lock ----------
LOCK_FILE = r"C:\ProgramData\SHCS\agent.lock"
os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)

try:
    lock = open(LOCK_FILE, "w")
    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
except OSError:
    sys.exit(0)  # another instance already running
# ----------------------------------------

from agent import start_agent

if __name__ == "__main__":
    if "--agent" in sys.argv:
        start_agent()
