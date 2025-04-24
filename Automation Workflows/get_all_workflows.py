import slumber
import json
import sys
import os


__friendly_name__ = "Get A List Of All Workflows"


# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_all_workflows():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.automation.workflows.get(**params)
        
        print("\nAll workflows:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetWorkflows raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_all_workflows()
