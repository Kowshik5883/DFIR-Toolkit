import re
import json
import logging

def analyze_logs(log_data):
    """
    Parses system logs and detects anomalies.
    """
    anomalies = []
    log_patterns = {
        "unauthorized_access": r"unauthorized access",
        "failed_login": r"failed login",
        "malware_activity": r"malware detected"
    }
    
    for line in log_data.split("\n"):
        for category, pattern in log_patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                anomalies.append({"category": category, "log": line})
    
    return {"anomalies": anomalies}

if __name__ == "__main__":
    sample_log = """
    2025-02-18 10:30:21 - unauthorized access detected
    2025-02-18 11:00:45 - failed login attempt from IP 192.168.1.10
    2025-02-18 12:15:33 - malware detected in process ID 3421
    """
    
    result = analyze_logs(sample_log)
    print(json.dumps(result, indent=4))
