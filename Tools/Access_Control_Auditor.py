# Access_Control_Auditor.py

# Simulated access control data (replace this with your actual access control data)
access_controls = {
    'user1': ['resource1', 'resource2'],
    'user2': ['resource2', 'resource3'],
    'user3': ['resource1', 'resource3']
}

def audit_access_controls(username, resource):
    if username in access_controls and resource in access_controls[username]:
        print(f"User {username} has access to {resource}. Access controls are compliant.")
        return True
    else:
        print(f"Warning: User {username} does not have access to {resource}. Review access controls!")
        return False

def main():
    username = input("Enter the username to audit: ")
    resource = input("Enter the resource to check access controls: ")
    audit_access_controls(username, resource)

if __name__ == "__main__":
    main()

#This script simulates access control data using a dictionary (access_controls). 
#The audit_access_controls function checks if the specified user has access to the specified resource based on the simulated access control data.
#Remember to replace the simulated access control data with your actual access control mechanism, such as querying a database or an external system. Adjust the script to fit your specific access control requirements and data structure."""
