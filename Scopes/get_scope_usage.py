import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_scope_usage(scope_id=None):
    # If scope_id wasn't provided as an argument, ask for it
    if scope_id is None:
        scope_id = input("Enter scope ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.scopes(scope_id).usage.get(**params)
        
        print("\nScope usage details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetScopeUsage raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_scope_usage()
