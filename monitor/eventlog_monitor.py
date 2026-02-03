import win32evtlog

FAILED_LOGIN_EVENT = 4625

def get_failed_logins():
    try:
        server = 'localhost'
        logtype = 'Security'
        hand = win32evtlog.OpenEventLog(server, logtype)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        count = 0
        events = win32evtlog.ReadEventLog(hand, flags, 0)

        for event in events:
            if event.EventID == FAILED_LOGIN_EVENT:
                count += 1
            if count > 5:
                break

        return count

    except Exception:
        # No admin privilege → safe fallback
        return 0

