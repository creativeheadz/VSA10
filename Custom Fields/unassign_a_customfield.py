import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def unassign_a_customfield(custom_field_id=None):
    # If custom_field_id wasn't provided as an argument, ask for it
    if custom_field_id is None:
        custom_field_id = input("Enter custom field ID: ")
    
    # Get the context type
    print("\nSelect context type:")
    print("1. Organization")
    print("2. Site")
    print("3. Group")
    print("4. Device")
    
    context_types = {
        "1": "Organization",
        "2": "Site",
        "3": "Group",
        "4": "Device"
    }
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in context_types:
            context_type = context_types[choice]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    # Get the context item ID
    context_item_id = input(f"Enter {context_type} ID: ")
    
    # Create the request body
    request_body = {
        "ContextType": context_type,
        "ContextItemId": context_item_id
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.customFields(custom_field_id).unassign.post(request_body)
        
        print("\nCustom field unassigned successfully:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nUnassignCustomField raised an exception:')
        print(str(e))

if __name__ == "__main__":
    unassign_a_customfield()
