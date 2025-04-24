import slumber
import json
import sys
import os

__friendly_name__ = "Get Script Executions"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_script_executions(script_id=None, device_id=None, top=50, skip=0):
    """
    Get executions of a specific script on a specific device
    
    Args:
        script_id (str): The ID of the script
        device_id (str): The device identifier
        top (int): Maximum number of records to return
        skip (int): Number of records to skip for pagination
        
    Returns:
        dict: The API response containing script executions
    """
    # If script_id wasn't provided as an argument, ask for it
    if script_id is None:
        script_id = input("Enter script ID: ")
    
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    # Ask for pagination parameters if they weren't provided
    if top is None:
        top_input = input("Enter maximum number of records to return (default 50): ")
        top = int(top_input) if top_input else 50
    
    if skip is None:
        skip_input = input("Enter number of records to skip (default 0): ")
        skip = int(skip_input) if skip_input else 0
    
    # Prepare parameters
    params = {'$top': str(top), '$skip': str(skip)}
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.scripts(script_id).device(device_id).executions.get(**params)
        
        print("\nScript execution history:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetScriptExecutions raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_script_executions()
