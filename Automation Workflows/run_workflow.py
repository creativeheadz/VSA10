import slumber
import json
import sys
import os
import requests

__friendly_name__ = "Run An Existing Workflow"


# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_user_input(prompt, default=None):
    """Get user input with an optional default value."""
    if default:
        user_input = input(f"{prompt} [{default}]: ")
        return user_input if user_input.strip() else default
    else:
        return input(f"{prompt}: ")

def run_workflow(workflow_id=None):
    # If workflow_id wasn't provided as an argument, ask for it
    if workflow_id is None:
        workflow_id = input("Enter workflow ID: ")
    
    # Ask if the user wants to specify device identifiers
    use_device_ids = input("Do you want to specify device identifiers? (y/n): ").lower().strip()
    
    # Initialize the request body - always include an empty structure even if no overrides
    request_body = {}
    
    if use_device_ids == 'y':
        # Get device identifiers as a comma-separated list
        device_ids_input = input("Enter device identifiers (comma separated): ")
        if device_ids_input.strip():
            device_ids = [id.strip() for id in device_ids_input.split(',')]
            request_body["DeviceIdentifiers"] = device_ids
    
    # Ask for optional webhook URL
    webhook_url = input("Enter webhook URL (optional, press Enter to skip): ").strip()
    if webhook_url:
        request_body["WebhookUrl"] = webhook_url
    
    # Ask for optional constant variable overrides
    add_variables = input("Do you want to add constant variable overrides? (y/n): ").lower().strip()
    if add_variables == 'y':
        variable_overrides = []
        
        while True:
            var_name = input("Enter variable name (or press Enter to finish): ").strip()
            if not var_name:
                break
                
            var_value = input(f"Enter value for {var_name}: ").strip()
            variable_overrides.append({
                "Name": var_name,
                "Value": var_value
            })
        
        if variable_overrides:
            request_body["ConstantVariableOverrides"] = variable_overrides
    
    try:
        print("\nSending workflow execution request with payload:")
        print(json.dumps(request_body, indent=4))
        
        # Use direct requests to get more detailed error information
        url = f"{config.ENDPOINT.rstrip('/')}/automation/workflows/{workflow_id}/run"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.post(
            url,
            json=request_body,
            auth=(config.TOKEN_ID, config.TOKEN_SECRET),
            headers=headers
        )
        
        # Try to parse the response as JSON
        try:
            result = response.json()
            print(f"\nResponse status code: {response.status_code}")
            print("Workflow execution result:")
            print(json.dumps(result, indent=4))
        except json.JSONDecodeError:
            print(f"\nResponse status code: {response.status_code}")
            print("Response content (not JSON):")
            print(response.text)
        
        # Check if the request was not successful
        if not response.ok:
            print(f"\nError: The server returned status code {response.status_code}")
            if 'Error' in result:
                print(f"Error message: {result.get('Error', {}).get('Message', 'No message provided')}")
                if 'Details' in result.get('Error', {}):
                    print(f"Error details: {result['Error']['Details']}")
        
    except Exception as e:
        print('\nRunWorkflow raised an exception:')
        print(str(e))

if __name__ == "__main__":
    run_workflow()
