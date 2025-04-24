import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_script_execution_details(script_id=None, device_id=None, execution_id=None):
    """
    Get detailed information about a specific script execution
    
    Args:
        script_id (str): The ID of the script
        device_id (str): The device identifier
        execution_id (str): The execution ID to retrieve details for
        
    Returns:
        dict: The API response containing execution details
    """
    # If script_id wasn't provided as an argument, ask for it
    if script_id is None:
        script_id = input("Enter script ID: ")
    
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
        
    # If execution_id wasn't provided as an argument, ask for it
    if execution_id is None:
        execution_id = input("Enter execution ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.scripts(script_id).device(device_id).executions(execution_id).get()
        
        print("\nScript execution details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetScriptExecution raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_script_execution_details()
