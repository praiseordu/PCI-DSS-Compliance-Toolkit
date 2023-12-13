# PCI_Compliance_Tool.py

import re

def check_password_compliance(password):
    # Check password length
    if len(password) < 12:
        return False, "Password must be at least 12 characters long."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, "Password meets PCI DSS compliance requirements."

def main():
    password = input("Enter the password to check for PCI DSS compliance: ")
    is_compliant, message = check_password_compliance(password)

    if is_compliant:
        print("Password is compliant with PCI DSS requirements.")
    else:
        print(f"Password is not compliant: {message}")

if __name__ == "__main__":
    main()
