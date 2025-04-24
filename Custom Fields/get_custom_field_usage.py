import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_custom_field_usage(custom_field_id=None):
    # If custom_field_id wasn't provided as an argument, ask for it
    if custom_field_id is None:
        custom_field_id = input("Enter custom field ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.customFields(custom_field_id).usage.get(**params)
        
        print("\nCustom field usage details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetCustomFieldUsage raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_custom_field_usage()
