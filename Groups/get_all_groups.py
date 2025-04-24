import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Get All Groups"

def get_all_groups():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.groups.get(**params)
        
        print("\nAll groups:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetGroups raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_all_groups()
