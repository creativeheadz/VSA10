import slumber
import json
import sys
import os

__friendly_name__ = "Get a Specific Script"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_script(script_id=None):
    """
    Get details for a specific automation script
    
    Args:
        script_id (str): The ID of the script to retrieve
        
    Returns:
        dict: The API response containing script details
    """
    # If script_id wasn't provided as an argument, ask for it
    if script_id is None:
        script_id = input("Enter script ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.scripts(script_id).get()
        
        print("\nScript details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetScript raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_a_specific_script()
