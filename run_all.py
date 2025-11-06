import subprocess
import time
import os

VENV_PYTHON = r"C:\Users\pushp\OneDrive\Desktop\Projects\SysSentry\venv\Scripts\python.exe"

processes = []

try:
    # Run monitor
    p1 = subprocess.Popen([VENV_PYTHON, "monitor.py"])
    processes.append(p1)

    # Run alerts
    p2 = subprocess.Popen([VENV_PYTHON, "alerts.py"])
    processes.append(p2)

    # Run diagnostics
    p3 = subprocess.Popen([VENV_PYTHON, "diagnostics.py"])
    processes.append(p3)

    # Run dashboard
    p4 = subprocess.Popen([VENV_PYTHON, "-m", "streamlit", "run", "dashboard.py"])
    processes.append(p4)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
    for p in processes:
        p.kill()
