import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Create an Organisation"

def create_an_organisation(name=None):
    """
    Create a new organisation
    
    Args:
        name (str): Name of the organisation
        
    Returns:
        dict: The API response containing the created organisation
    """
    # If name wasn't provided as an argument, ask for it
    if name is None:
        name = input("Enter organisation name: ")
    
    # Prepare request body
    request_body = {
        "Name": name
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.organizations.post(request_body)
        
        print("\nOrganisation created successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nCreateOrganization raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    create_an_organisation()
