import slumber
import json
import sys
import os

# Define a friendly name for this script
__friendly_name__ = "Create a new site in the system"

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def create_a_site(name=None, parent_id=None, contact_info=None):
    """
    Create a new site
    
    Args:
        name (str): Name of the site
        parent_id (int): ID of the parent site
        contact_info (dict): Dictionary containing contact information
        
    Returns:
        dict: The API response containing the created site
    """
    # If name wasn't provided as an argument, ask for it
    if name is None:
        name = input("Enter site name: ")
    
    # If parent_id wasn't provided as an argument, ask for it
    if parent_id is None:
        parent_id_input = input("Enter parent ID (leave blank if none): ")
        parent_id = int(parent_id_input) if parent_id_input.strip() else None
    
    # If contact_info wasn't provided, create it interactively
    if contact_info is None:
        contact_info = {}
        print("\nEnter contact information (press Enter to skip any field):")
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
    
    # Add optional fields if provided
    if parent_id is not None:
        request_body["ParentId"] = parent_id
    
    if contact_info:
        request_body["ContactInformation"] = contact_info
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.sites.post(request_body)
        
        print("\nSite created successfully:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nCreateSite raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    create_a_site()
