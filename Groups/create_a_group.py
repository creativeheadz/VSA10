import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Create a Group"

def get_user_input(prompt, default=None):
    """Get user input with an optional default value."""
    if default:
        user_input = input(f"{prompt} [{default}]: ")
        return user_input if user_input.strip() else default
    else:
        return input(f"{prompt}: ")

def create_a_group():
    print("\n=== Create a New Group ===")
    
    # Get user input for required fields
    group_name = input("Enter Group Name (required): ")
    while not group_name.strip():
        print("Group Name is required.")
        group_name = input("Enter Group Name (required): ")
    
    parent_id_input = input("Enter Parent Site ID (required): ")
    try:
        parent_id = int(parent_id_input)
    except ValueError:
        print("Invalid Parent Site ID. It must be an integer.")
        return
    
    # Get optional notes
    notes = input("Enter Group Notes (optional): ")
    
    # Create the request body
    request_body = {
        "Name": group_name,
        "ParentId": parent_id
    }
    
    # Add notes if provided
    if notes.strip():
        request_body["Notes"] = notes
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.groups.post(request_body)
        
        print("\nGroup created successfully:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nCreateGroup raised an exception:')
        print(str(e))

if __name__ == "__main__":
    create_a_group()
