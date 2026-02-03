import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "shcs.log")


def read_last_logs(lines=200):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            recent = all_lines[-lines:]
            recent.reverse()
            return "".join(recent)
    except Exception:
        return "No logs available.\n"

