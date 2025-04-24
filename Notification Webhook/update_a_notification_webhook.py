import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Update a Notification Webhook"

def update_a_notification_webhook(webhook_id=None, name=None, description=None, priorities=None, 
                                 organization_ids=None, headers=None, url=None, 
                                 language=None):
    """
    Update an existing notification webhook
    
    Args:
        webhook_id (str): ID of the webhook to update
        name (str): Updated name of the webhook
        description (str): Updated description of the webhook
        priorities (list): Updated list of priority levels
        organization_ids (list): Updated list of organization IDs
        headers (dict): Updated custom headers for the webhook
        url (str): Updated URL endpoint for the webhook
        language (str): Updated language code
        
    Returns:
        dict: The API response containing the updated webhook
    """
    # If webhook_id wasn't provided as an argument, ask for it
    if webhook_id is None:
        webhook_id = input("Enter webhook ID to update: ")
    
    # Prompt for parameters if not provided
    if name is None:
        name = input("Enter updated webhook name: ")
    
    if description is None:
        description = input("Enter updated webhook description: ")
    
    if priorities is None:
        print("Enter updated priorities (comma-separated, available options: Low, Normal, Elevated, Critical)")
        priorities_input = input("Default [Low,Normal,Elevated,Critical]: ")
        if priorities_input:
            priorities = [p.strip() for p in priorities_input.split(",")]
        else:
            priorities = ["Low", "Normal", "Elevated", "Critical"]
    
    if organization_ids is None:
        org_ids_input = input("Enter updated organization IDs (comma-separated integers): ")
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
        url = input("Enter updated webhook URL: ")
    
    if language is None:
        language_input = input("Enter updated language code (default: en): ")
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
        result = api.notifications.webhooks(webhook_id).put(request_body)
        
        print("\nWebhook updated successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nUpdateNotificationWebhook raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    update_a_notification_webhook()
