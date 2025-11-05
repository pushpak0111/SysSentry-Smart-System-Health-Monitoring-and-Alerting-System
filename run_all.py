import subprocess
import time
import threading

# ---------------------------
# Function to run monitor.py continuously
# ---------------------------
def run_monitor():
    subprocess.run(["python", "monitor.py"])

# ---------------------------
# Function to run alerts.py periodically (every 10 seconds)
# ---------------------------
def run_alerts():
    while True:
        subprocess.run(["python", "alerts.py"])
        time.sleep(10)  # check every 10 seconds

# ---------------------------
# Function to run dashboard.py (Streamlit)
# ---------------------------
def run_dashboard():
    subprocess.run(["streamlit", "run", "dashboard.py"])

# ---------------------------
# Run all three scripts using threads
# ---------------------------
if __name__ == "__main__":
    t1 = threading.Thread(target=run_monitor)
    t2 = threading.Thread(target=run_alerts)
    t3 = threading.Thread(target=run_dashboard)

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Keep main thread alive
    t1.join()
    t2.join()
    t3.join()
