import slumber
import json
import sys
import os
__friendly_name__ = "Get A List Of Applied Policies For A Specific Device"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_device_applied_policies(device_id=None):
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.devices(device_id).appliedpolicies.get()
        
        print("\nDevice applied policies:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetDeviceAppliedPolicies raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_device_applied_policies()
