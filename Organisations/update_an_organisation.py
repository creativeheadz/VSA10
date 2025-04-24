import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Update an Organisation"

def update_an_organisation(organisation_id=None, name=None):
    """
    Update an existing organisation
    
    Args:
        organisation_id (str): ID of the organisation to update
        name (str): New name for the organisation
        
    Returns:
        dict: The API response containing the updated organisation
    """
    # If organisation_id wasn't provided as an argument, ask for it
    if organisation_id is None:
        organisation_id = input("Enter organisation ID to update: ")
    
    # If name wasn't provided as an argument, ask for it
    if name is None:
        name = input("Enter new organisation name: ")
    
    # Prepare request body
    request_body = {
        "Name": name
    }
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.organizations(organisation_id).put(request_body)
        
        print("\nOrganisation updated successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nUpdateOrganization raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    update_an_organisation()
