import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Send a Notification"

def notify(instance_id=None, title=None, message=None, priority=None):
    """
    Send a notification through the API
    
    Args:
        instance_id (str): The instance ID (typically a UUID)
        title (str): Title of the notification
        message (str): Message content of the notification
        priority (str): Priority level (low, normal, elevated, critical)
        
    Returns:
        dict: The API response after sending the notification
    """
    # If instance_id wasn't provided as an argument, ask for it
    if instance_id is None:
        instance_id = input("Enter instance ID (UUID): ")
    
    # If title wasn't provided as an argument, ask for it
    if title is None:
        title = input("Enter notification title: ")
    
    # If message wasn't provided as an argument, ask for it
    if message is None:
        message = input("Enter notification message: ")
    
    # If priority wasn't provided, prompt with valid options
    if priority is None:
        print("Enter priority (available options: low, normal, elevated, critical)")
        priority = input("Priority [normal]: ").lower() or "normal"
    
    # Prepare request body
    request_body = {
        "InstanceId": instance_id,
        "Title": title,
        "Message": message,
        "Priority": priority,
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications.post(request_body)
        
        print("\nNotification sent successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nNotify raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    notify()
