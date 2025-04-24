import slumber
import json
import sys
import os
__friendly_name__ = "Get Environment Information"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_environment_information():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.environment.get()
        
        print("\nEnvironment information:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetEnvironmentInformation raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_environment_information()
