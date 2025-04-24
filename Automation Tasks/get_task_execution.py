import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_task_execution(execution_id=None):
    # If execution_id wasn't provided as an argument, ask for it
    if execution_id is None:
        execution_id = input("Enter task execution ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.tasks.executions(execution_id).get()
        
        print("\nTask execution details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetTaskExecution raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_task_execution()
