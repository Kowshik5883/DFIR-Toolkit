import os
import hashlib
import psutil

def load_signature_database(signature_file):
    """Loads known threat signatures from a file."""
    signatures = {}
    with open(signature_file, "r") as file:
        for line in file:
            hash_value, description = line.strip().split(" ", 1)
            signatures[hash_value] = description
    return signatures

def calculate_file_hash(file_path):
    """Calculates SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def scan_running_processes(signatures):
    """Scans running processes for potential threats."""
    detected = []
    for process in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if process.info['exe']:
                file_hash = calculate_file_hash(process.info['exe'])
                if file_hash and file_hash in signatures:
                    detected.append((process.info['name'], process.info['pid'], signatures[file_hash]))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return detected

if __name__ == "__main__":
    signature_file = "threat_signatures.txt"  # Replace with actual signature database
    
    signatures = load_signature_database(signature_file)
    threats = scan_running_processes(signatures)
    
    if threats:
        for name, pid, description in threats:
            print(f"Threat detected: {name} (PID: {pid}) - {description}")
    else:
        print("No threats detected in running processes.")
