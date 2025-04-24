import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_workflow_executions():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.automation.workflows.executions.get(**params)
        
        print("\nWorkflow executions:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetWorkflowExecutions raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_workflow_executions()
