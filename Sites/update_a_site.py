import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

__friendly_name__ = "Update a Site"

def update_a_site(site_id=None, name=None, contact_info=None):
    """
    Update an existing site
    
    Args:
        site_id (str): ID of the site to update
        name (str): Updated name for the site
        contact_info (dict): Updated contact information
        
    Returns:
        dict: The API response containing the updated site
    """
    # If site_id wasn't provided as an argument, ask for it
    if site_id is None:
        site_id = input("Enter site ID to update: ")
    
    # If name wasn't provided as an argument, ask for it
    if name is None:
        name = input("Enter updated site name: ")
    
    # If contact_info wasn't provided, create it interactively
    if contact_info is None:
        contact_info = {}
        print("\nEnter updated contact information (press Enter to skip any field):")
        contact_info["Phone"] = input("Phone: ").strip() or None
        contact_info["Fax"] = input("Fax: ").strip() or None
        contact_info["Email"] = input("Email: ").strip() or None
        contact_info["ContactName"] = input("Contact Name: ").strip() or None
        contact_info["CountryCode"] = input("Country Code (e.g., US): ").strip() or None
        contact_info["City"] = input("City: ").strip() or None
        contact_info["Address1"] = input("Address Line 1: ").strip() or None
        contact_info["Address2"] = input("Address Line 2: ").strip() or None
        contact_info["Zip"] = input("Zip/Postal Code: ").strip() or None
        
        # Remove None values from contact_info
        contact_info = {k: v for k, v in contact_info.items() if v is not None}
    
    # Prepare request body
    request_body = {
        "Name": name,
    }
    
    # Add contact information if provided
    if contact_info:
        request_body["ContactInformation"] = contact_info
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.sites(site_id).put(request_body)
        
        print("\nSite updated successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nUpdateSite raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    update_a_site()
