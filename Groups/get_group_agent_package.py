import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_group_agent_package(group_id=None):
    # If group_id wasn't provided as an argument, ask for it
    if group_id is None:
        group_id = input("Enter group ID: ")
    
    # Ask for architecture choice
    print("\nSelect agent architecture:")
    print("1. Windows (64 bit)")
    print("2. Windows (32 bit)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            package_type = "windows_agent_x64"
            break
        elif choice == "2":
            package_type = "windows_agent_x86"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.groups(group_id).package(package_type).get()
        
        print("\nGroup agent package information:")
        print(json.dumps(result, indent=4))
        
        # For easier access, also extract the URL directly
        if 'Data' in result and 'Url' in result['Data']:
            print("\nDirect installer URL:")
            print(result['Data']['Url'])
        
    except Exception as e:
        print('\nGetGroupPackage raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_group_agent_package()
