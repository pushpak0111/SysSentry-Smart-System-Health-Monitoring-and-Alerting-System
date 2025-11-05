import psutil
import time
import pandas as pd
from datetime import datetime
import os
from database import Metric, session   # ✅ import database session

METRICS_FILE = "data/metrics.csv"

def get_system_metrics():
    """Collect system performance metrics."""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }

def log_metrics():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        metric = Metric(
            cpu_percent=cpu,
            memory_percent=mem,
            disk_percent=disk
        )
        session.add(metric)
        session.commit()

        print(f"[{datetime.now()}] Logged: CPU={cpu}% | MEM={mem}% | DISK={disk}%")
        time.sleep(5)

if __name__ == "__main__":
    log_metrics()
