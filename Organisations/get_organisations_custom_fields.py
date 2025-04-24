import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Get Organisation Custom Fields"

def get_organisations_custom_fields(organisation_id=None, top=50, skip=0):
    """
    Get custom fields for a specific organization
    
    Args:
        organisation_id (str): ID of the organization
        top (int): Maximum number of records to return
        skip (int): Number of records to skip for pagination
        
    Returns:
        dict: The API response containing custom fields
    """
    # If organisation_id wasn't provided as an argument, ask for it
    if organisation_id is None:
        organisation_id = input("Enter organisation ID: ")
    
    # Ask for pagination parameters if they weren't provided
    if top is None:
        top_input = input("Enter maximum number of records to return (default 50): ")
        top = int(top_input) if top_input else 50
    
    if skip is None:
        skip_input = input("Enter number of records to skip (default 0): ")
        skip = int(skip_input) if skip_input else 0
    
    # Prepare parameters
    params = {'$top': str(top), '$skip': str(skip)}
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.organizations(organisation_id).customFields.get(**params)
        
        print("\nOrganisation custom fields:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetOrganizationCustomFields raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_organisations_custom_fields()
