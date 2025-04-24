import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Get Specific Notification Webhook"

def get_specific_notification_webhook(webhook_id=None):
    """
    Get details for a specific notification webhook
    
    Args:
        webhook_id (str): The ID of the webhook to retrieve
        
    Returns:
        dict: The API response containing webhook details
    """
    # If webhook_id wasn't provided as an argument, ask for it
    if webhook_id is None:
        webhook_id = input("Enter webhook ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications.webhooks(webhook_id).get()
        
        print("\nWebhook details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetNotificationWebhook raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_specific_notification_webhook()
