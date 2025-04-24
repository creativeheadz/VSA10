import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def run_task(task_id=None):
    # If task_id wasn't provided as an argument, ask for it
    if task_id is None:
        task_id = input("Enter task ID: ")
    
    # Ask if the user wants to specify device identifiers
    use_device_ids = input("Do you want to specify device identifiers? (y/n): ").lower().strip()
    
    # Initialize the request body
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
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.tasks(task_id).run.post(request_body)
        
        print("\nTask execution result:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nRunTask raised an exception:')
        print(str(e))

if __name__ == "__main__":
    run_task()
