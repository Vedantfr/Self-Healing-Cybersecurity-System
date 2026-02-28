import os

LOG_FILE = r"C:\ProgramData\SHCS\shcs.log"

def read_last_logs():
    try:
        if not os.path.exists(LOG_FILE):
            return ""

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

       
        lines.reverse()

        return "".join(lines)

    except Exception:
        return ""

