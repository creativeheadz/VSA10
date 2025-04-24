import slumber
import json
import sys
import os

__friendly_name__ = "Get Task Execution Scripts"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_task_execution_scripts(execution_id=None, device_id=None):
    # If execution_id wasn't provided as an argument, ask for it
    if execution_id is None:
        execution_id = input("Enter task execution ID: ")
    
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.tasks.executions(execution_id).devices(device_id).scripts.get()
        
        print("\nTask execution scripts:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetTaskExecutionScripts raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_task_execution_scripts()
