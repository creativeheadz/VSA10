import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def run_script(script_id=None, device_id=None, webhook_url=None, variables=None):
    """
    Run an automation script with the specified parameters
    
    Args:
        script_id (str): The ID of the script to run
        device_id (str): The device identifier to run the script on
        webhook_url (str): Optional URL to receive webhook notifications
        variables (list): Optional list of variable dictionaries with Id and Value
        
    Returns:
        dict: The API response
    """
    # If script_id wasn't provided as an argument, ask for it
    if script_id is None:
        script_id = input("Enter script ID: ")
    
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    # If webhook_url wasn't provided as an argument, ask for it
    if webhook_url is None:
        webhook_url = input("Enter webhook URL (or press Enter to skip): ")
        # If user skipped webhook_url, set it to None
        if webhook_url == "":
            webhook_url = None
    
    # Initialize variables if not provided
    if variables is None:
        variables = []
        add_variable = input("Do you want to add variables? (y/n): ").lower()
        while add_variable == 'y':
            var_id = input("Enter variable ID: ")
            var_value = input("Enter variable value: ")
            variables.append({
                "Id": int(var_id),
                "Value": var_value
            })
            add_variable = input("Add another variable? (y/n): ").lower()
    
    # Prepare request body
    request_body = {
        "DeviceIdentifier": device_id
    }
    
    # Add webhook URL if provided
    if webhook_url:
        request_body["WebhookUrl"] = webhook_url
    
    # Add variables if provided
    if variables:
        request_body["Variables"] = variables
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.scripts(script_id).run.post(request_body)
        
        print("\nScript execution result:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nRunScript raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    run_script()
