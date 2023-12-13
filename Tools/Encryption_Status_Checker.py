# Encryption_Status_Checker.py
import subprocess

def check_disk_encryption_status(device_path):
    if is_disk_encrypted(device_path):
        print(f"The disk {device_path} is encrypted.")
    else:
        print(f"Warning: The disk {device_path} is not encrypted!")

def is_disk_encrypted(device_path):
    try:
        # Example: Use the 'lsblk' command to check if the disk is encrypted
        output = subprocess.check_output(['lsblk', '-o', 'NAME,TYPE,CRYPT'])
        output_lines = output.decode('utf-8').split('\n')

        for line in output_lines:
            if device_path in line and 'crypt' in line:
                return True

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    return False

def main():
    device_path = input("Enter the path of the device to check for encryption status: ")
    check_disk_encryption_status(device_path)

if __name__ == "__main__":
    main()
