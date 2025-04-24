import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_customfield(custom_field_id=None):
    # If custom_field_id wasn't provided as an argument, ask for it
    if custom_field_id is None:
        custom_field_id = input("Enter custom field ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.customFields(custom_field_id).get()
        
        print("\nCustom field details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetCustomField raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_a_specific_customfield()
