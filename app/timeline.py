import os
import datetime

def create_timeline(log_file):
    """
    Generates a timeline of events from system logs.
    """
    timeline = []
    
    with open(log_file, "r") as file:
        for line in file:
            parts = line.strip().split(" - ")
            if len(parts) == 2:
                timestamp, event = parts
                try:
                    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    timeline.append({"timestamp": dt, "event": event})
                except ValueError:
                    continue
    
    timeline.sort(key=lambda x: x["timestamp"])  # Sort events chronologically
    return timeline

if __name__ == "__main__":
    log_file_path = "system_logs.txt"  # Replace with actual log file path
    timeline_data = create_timeline(log_file_path)
    for event in timeline_data:
        print(f"{event['timestamp']} - {event['event']}")
