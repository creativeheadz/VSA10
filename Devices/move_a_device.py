import slumber
import json
import sys
import os
__friendly_name__ = "Move a Device"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_user_input(prompt, default):
    """Get user input with a default value."""
    user_input = input(f"{prompt} [{default}]: ")
    return user_input if user_input.strip() else default

def move_a_device(device_id=None):
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    # Default group ID
    default_group_id = 125
    
    # Get user input for group ID
    group_id_input = get_user_input("Enter new Group ID", str(default_group_id))
    
    # Validate group ID is an integer
    try:
        group_id = int(group_id_input)
    except ValueError:
        print(f"Invalid Group ID. Using default: {default_group_id}")
        group_id = default_group_id
    
    # Create the request body
    request_body = {
        "GroupId": group_id
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.devices(device_id).move.put(request_body)
        print("\nDevice moved successfully:")
        print(json.dumps(result, indent=4))
    except Exception as e:
        print('\nMoveDevice raised an exception:')
        print(str(e))

if __name__ == "__main__":
    move_a_device()
