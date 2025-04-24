import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_global_rules():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.patchmanagement.globalrules.get()
        
        print("\nPatch Management Global Rules:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetGlobalRules raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_global_rules()
