# File_Integrity_Monitoring_Tool.py

import hashlib

def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def monitor_file_integrity(file_path, baseline_hash):
    current_hash = calculate_file_hash(file_path)
    if current_hash != baseline_hash:
        print(f"File {file_path} has been modified! Current hash: {current_hash}")
    else:
        print(f"File {file_path} is unchanged.")

def main():
    file_path = input("Enter the path to the file for integrity monitoring: ")
    baseline_hash = calculate_file_hash(file_path)
    print(f"Baseline hash for {file_path}: {baseline_hash}")

    while True:
        input("Press Enter to check file integrity...")
        monitor_file_integrity(file_path, baseline_hash)

if __name__ == "__main__":
    main()
