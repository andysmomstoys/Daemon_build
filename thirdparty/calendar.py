import datetime

def get_current_datetime():
    """Return current date and time info"""
    now = datetime.datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "weekday": now.strftime("%A")
    }
