import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_specific_group(group_id=None):
    # If group_id wasn't provided as an argument, ask for it
    if group_id is None:
        group_id = input("Enter group ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.groups(group_id).get()
        
        print("\nGroup details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetGroup raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_specific_group()
