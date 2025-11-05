# diagnostics.py
# This module provides suggestions for fixing common system alerts

def suggest_fix(alert):
    # Dictionary mapping alert messages to suggested fixes
    fixes = {
        "High CPU Usage": "Close background apps or restart resource-heavy processes.",
        "High Memory Usage": "Restart memory-intensive apps or clear system cache.",
        "Disk Almost Full": "Delete temporary/log files or remove unused data."
    }
    # Return the matching fix or a default message
    return fixes.get(alert, "No suggestion available.")
