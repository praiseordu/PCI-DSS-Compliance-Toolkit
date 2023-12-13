# Encryption_Status_Checker.py

def check_disk_encryption_status(device_path):
    # Simulate checking the encryption status of a disk
    if is_disk_encrypted(device_path):
        print(f"The disk {device_path} is encrypted.")
    else:
        print(f"Warning: The disk {device_path} is not encrypted!")

def is_disk_encrypted(device_path):
    # Simulate checking if the disk is encrypted
    # Add actual logic for checking disk encryption status
    return True

def main():
    device_path = input("Enter the path of the device to check for encryption status: ")
    check_disk_encryption_status(device_path)

if __name__ == "__main__":
    main()
