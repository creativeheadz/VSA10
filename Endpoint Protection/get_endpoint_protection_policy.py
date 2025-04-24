import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_endpoint_protection_policy(policy_id=None):
    # If policy_id wasn't provided as an argument, ask for it
    if policy_id is None:
        policy_id = input("Enter endpoint protection policy ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.endpointprotection.policies(policy_id).get()
        
        print("\nEndpoint protection policy details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetPolicy raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_endpoint_protection_policy()
