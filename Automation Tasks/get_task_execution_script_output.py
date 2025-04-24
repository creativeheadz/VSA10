import slumber
import json
import sys
import os

__friendly_name__ = "Get Task Execution Script Output"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_task_execution_script_output(execution_id=None, device_id=None, script_id=None):
    # If execution_id wasn't provided as an argument, ask for it
    if execution_id is None:
        execution_id = input("Enter task execution ID: ")
    
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
        
    # If script_id wasn't provided as an argument, ask for it
    if script_id is None:
        script_id = input("Enter script identifier: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.tasks.executions(execution_id).devices(device_id).scripts(script_id).get()
        
        print("\nTask execution script output:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetTaskExecutionScriptOutput raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_task_execution_script_output()
