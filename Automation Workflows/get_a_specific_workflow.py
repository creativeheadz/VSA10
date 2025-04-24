import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_workflow(workflow_id=None):
    # If workflow_id wasn't provided as an argument, ask for it
    if workflow_id is None:
        # Ask for the workflow ID
        workflow_id = input("Enter workflow ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.workflows(workflow_id).get()
        
        print("\nWorkflow details:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetWorkflow raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_a_specific_workflow()
