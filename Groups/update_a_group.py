import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def update_a_group(group_id=None):
    # If group_id wasn't provided as an argument, ask for it
    if group_id is None:
        group_id_input = input("Enter Group ID to update: ")
        try:
            group_id = group_id_input.strip()
        except ValueError:
            print("Invalid Group ID.")
            return
    
    print("\n=== Update Group Information ===")
    
    # Get current group information to show as defaults
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        current_group = api.groups(group_id).get()
        
        if 'Data' in current_group:
            current_name = current_group['Data'].get('Name', '')
            current_notes = current_group['Data'].get('Notes', '')
            print(f"Current Group Name: {current_name}")
            print(f"Current Group Notes: {current_notes}")
        else:
            current_name = ''
            current_notes = ''
            print("Could not retrieve current group information.")
    except Exception as e:
        print(f"Error retrieving current group information: {str(e)}")
        current_name = ''
        current_notes = ''
    
    # Get user input for fields to update
    print("\nEnter new values (leave blank to keep current values):")
    new_name = input(f"New Group Name: ")
    new_notes = input(f"New Group Notes: ")
    
    # Use current values if new ones are not provided
    group_name = new_name if new_name.strip() else current_name
    group_notes = new_notes if new_notes.strip() else current_notes
    
    # Create the request body
    request_body = {
        "Name": group_name
    }
    
    # Add notes if provided
    if group_notes:
        request_body["Notes"] = group_notes
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.groups(group_id).put(request_body)
        
        print("\nGroup updated successfully:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nUpdateGroup raised an exception:')
        print(str(e))

if __name__ == "__main__":
    update_a_group()
