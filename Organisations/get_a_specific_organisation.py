import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_organisation(organisation_id=None):
    """
    Get details for a specific organisation
    
    Args:
        organisation_id (str): The ID of the organisation to retrieve
        
    Returns:
        dict: The API response containing organisation details
    """
    # If organisation_id wasn't provided as an argument, ask for it
    if organisation_id is None:
        organisation_id = input("Enter organisation ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.organizations(organisation_id).get()
        
        print("\nOrganisation details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetOrganization raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_a_specific_organisation()
