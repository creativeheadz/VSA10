import slumber
import json
import sys
import os

__friendly_name__ = "Get a Specific Task"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_task(task_id=None):
    """
    Get details for a specific automation task
    
    Args:
        task_id (str): The ID of the task to retrieve
        
    Returns:
        dict: The API response containing task details
    """
    # If task_id wasn't provided as an argument, ask for it
    if task_id is None:
        task_id = input("Enter task ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.automation.tasks(task_id).get()
        
        print("\nTask details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetTask raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_a_specific_task()
