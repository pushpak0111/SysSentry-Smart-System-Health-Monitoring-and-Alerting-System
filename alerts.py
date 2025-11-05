from datetime import datetime
from plyer import notification
from database import Alert, session
import pandas as pd
import os

CPU_THRESHOLD = 85
MEM_THRESHOLD = 80
DISK_THRESHOLD = 85
METRICS_FILE = "data/metrics.csv"

def log_alert(message):
    alert = Alert(timestamp=datetime.now(), alert=message)
    session.add(alert)
    session.commit()
    print(f"[ALERT] {message} stored in Supabase")

def notify_user(message):
    notification.notify(
        title="⚠️ SysSentry Alert",
        message=message,
        timeout=5
    ) # type: ignore

def check_for_alerts():
    df = pd.read_csv(METRICS_FILE)
    latest = df.iloc[-1]

    if latest['cpu_percent'] > CPU_THRESHOLD:
        log_alert("High CPU Usage")
        notify_user("High CPU Usage Detected")

    if latest['memory_percent'] > MEM_THRESHOLD:
        log_alert("High Memory Usage")
        notify_user("High Memory Usage Detected")

    if latest['disk_percent'] > DISK_THRESHOLD:
        log_alert("Disk Almost Full")
        notify_user("Disk Space Almost Full")

if __name__ == "__main__":
    check_for_alerts()
