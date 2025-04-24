import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def regenerate_webhook_secret_key(webhook_id=None):
    """
    Regenerate the secret key for a notification webhook
    
    Args:
        webhook_id (str): ID of the webhook to regenerate secret key for
        
    Returns:
        dict: The API response containing the new secret key
    """
    # If webhook_id wasn't provided as an argument, ask for it
    if webhook_id is None:
        webhook_id = input("Enter webhook ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.notifications.webhooks(webhook_id).regenerateSecretKey.post()
        
        print("\nSecret key regenerated successfully:")
        print(f"New Secret Key: {result['Data']['SecretKey']}")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nRegenerateSecretKey raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    regenerate_webhook_secret_key()
