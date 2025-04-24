import slumber
import json
import sys
import os
__friendly_name__ = "Assign a Custom Field"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def assign_a_custom_field(custom_field_id=None):
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
    
    # Ask about default value
    use_default = input("Use default value (y/n)? ").lower().strip()
    use_default_value = use_default == 'y'
    
    # If not using default, get the custom value
    value = None
    if not use_default_value:
        value = input("Enter custom field value: ")
    
    # Create the request body
    request_body = {
        "ContextType": context_type,
        "ContextItemId": context_item_id,
        "UseDefaultValue": use_default_value
    }
    
    # Only add Value if not using default
    if not use_default_value and value is not None:
        request_body["Value"] = value
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.customFields(custom_field_id).assign.post(request_body)
        
        print("\nCustom field assigned successfully:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nAssignCustomField raised an exception:')
        print(str(e))

if __name__ == "__main__":
    assign_a_custom_field()
