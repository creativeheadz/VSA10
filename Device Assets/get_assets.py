import slumber
import json
import sys
import os
__friendly_name__ = "Get Assets"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_assets():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.assets.get(**params)
        
        print("\nAssets information:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetAssets raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_assets()
