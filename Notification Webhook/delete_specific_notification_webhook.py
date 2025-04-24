import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Delete A Specific Notification Webhook"

def delete_specific_notification_webhook(webhook_id=None):
    """
    Delete a specific notification webhook
    
    Args:
        webhook_id (str): The ID of the webhook to delete
        
    Returns:
        dict: The API response after deletion
    """
    # If webhook_id wasn't provided as an argument, ask for it
    if webhook_id is None:
        webhook_id = input("Enter webhook ID to delete: ")
    
    # Confirm deletion
    confirmation = input(f"Are you sure you want to delete webhook {webhook_id}? (y/n): ").lower()
    if confirmation != 'y':
        print("Deletion cancelled.")
        return None
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications.webhooks(webhook_id).delete()
        
        print("\nWebhook deleted successfully.")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nDeleteNotificationWebhook raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    delete_specific_notification_webhook()
