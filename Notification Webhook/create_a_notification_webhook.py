import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def create_a_notification_webhook(name=None, description=None, priorities=None, 
                                 organization_ids=None, headers=None, url=None, 
                                 language=None):
    """
    Create a new notification webhook
    
    Args:
        name (str): Name of the webhook
        description (str): Description of the webhook
        priorities (list): List of priority levels
        organization_ids (list): List of organization IDs
        headers (dict): Custom headers for the webhook
        url (str): URL endpoint for the webhook
        language (str): Language code
        
    Returns:
        dict: The API response containing the created webhook
    """
    # Prompt for parameters if not provided
    if name is None:
        name = input("Enter webhook name: ")
    
    if description is None:
        description = input("Enter webhook description: ")
    
    if priorities is None:
        print("Enter priorities (comma-separated, available options: Low, Normal, Elevated, Critical)")
        priorities_input = input("Default [Low,Normal,Elevated,Critical]: ")
        if priorities_input:
            priorities = [p.strip() for p in priorities_input.split(",")]
        else:
            priorities = ["Low", "Normal", "Elevated", "Critical"]
    
    if organization_ids is None:
        org_ids_input = input("Enter organization IDs (comma-separated integers): ")
        organization_ids = [int(id.strip()) for id in org_ids_input.split(",") if id.strip()]
    
    if headers is None:
        headers = {}
        add_header = input("Do you want to add custom headers? (y/n): ").lower()
        while add_header == 'y':
            header_key = input("Enter header key: ")
            header_value = input("Enter header value: ")
            headers[header_key] = header_value
            add_header = input("Add another header? (y/n): ").lower()
    
    if url is None:
        url = input("Enter webhook URL: ")
    
    if language is None:
        language_input = input("Enter language code (default: en): ")
        language = language_input if language_input else "en"
    
    # Prepare request body
    request_body = {
        "Name": name,
        "Description": description,
        "Priorities": priorities,
        "OrganizationIds": organization_ids,
        "Headers": headers,
        "Url": url,
        "Language": language
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications.webhooks.post(request_body)
        
        print("\nWebhook created successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nCreateNotificationWebhook raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    create_a_notification_webhook()
