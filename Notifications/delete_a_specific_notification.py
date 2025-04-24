import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Delete a Specific Notification"

def delete_a_specific_notification(notification_id=None):
    """
    Delete a specific notification
    
    Args:
        notification_id (str): The ID of the notification to delete
        
    Returns:
        dict: The API response after deletion
    """
    # If notification_id wasn't provided as an argument, ask for it
    if notification_id is None:
        notification_id = input("Enter notification ID to delete: ")
    
    # Confirm deletion
    confirmation = input(f"Are you sure you want to delete notification {notification_id}? (y/n): ").lower()
    if confirmation != 'y':
        print("Deletion cancelled.")
        return None
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications(notification_id).delete()
        
        print("\nNotification deleted successfully.")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nDeleteNotification raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    delete_a_specific_notification()
