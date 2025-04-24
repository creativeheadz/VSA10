import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Get a Specific Notification"

def get_a_specific_notification(notification_id=None):
    """
    Get details for a specific notification
    
    Args:
        notification_id (str): The ID of the notification to retrieve
        
    Returns:
        dict: The API response containing notification details
    """
    # If notification_id wasn't provided as an argument, ask for it
    if notification_id is None:
        notification_id = input("Enter notification ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications(notification_id).get()
        
        print("\nNotification details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetNotification raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_a_specific_notification()
