# Access_Control_Auditor.py

def audit_access_controls(username, resource):
    # Simulate checking access controls for a user and a resource
    if has_access(username, resource):
        print(f"User {username} has access to {resource}. Access controls are compliant.")
    else:
        print(f"Warning: User {username} does not have access to {resource}. Review access controls!")

def has_access(username, resource):
    # Simulate checking if the user has access to the resource
    # Add actual logic for checking access controls
    return True

def main():
    username = input("Enter the username to audit: ")
    resource = input("Enter the resource to check access controls: ")
    audit_access_controls(username, resource)

if __name__ == "__main__":
    main()
