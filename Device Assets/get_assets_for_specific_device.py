import slumber
import json
import sys
import os
__friendly_name__ = "Get Assets for a Specific Device"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_assets_for_specific_device(device_id=None):
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.assets(device_id).get()
        
        print("\nAssets for device:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetDeviceAssets raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_assets_for_specific_device()
