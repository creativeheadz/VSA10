import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_workflow_execution_details(execution_id=None):
    # If execution_id wasn't provided as an argument, ask for it
    if execution_id is None:
        # Ask for the execution ID as an integer
        while True:
            try:
                execution_id = int(input("Enter workflow execution ID: "))
                break
            except ValueError:
                print("Please enter a valid integer for the execution ID.")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.workflows.executions(str(execution_id)).get()
        
        print("\nWorkflow execution details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetWorkflowExecutionDetails raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_workflow_execution_details()
