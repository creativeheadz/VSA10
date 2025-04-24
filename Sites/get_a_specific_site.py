import slumber
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_a_specific_site(site_id=None):
    """
    Get details for a specific site
    
    Args:
        site_id (str): The ID of the site to retrieve
        
    Returns:
        dict: The API response containing site details
    """
    # If site_id wasn't provided as an argument, ask for it
    if site_id is None:
        site_id = input("Enter site ID: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.sites(site_id).get()
        
        print("\nSite details:")
        print(json.dumps(result, indent=4))
        
        return result
        
    except Exception as e:
        print('\nGetSite raised an exception:')
        print(str(e))
        return None

if __name__ == "__main__":
    get_a_specific_site()
