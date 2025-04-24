import slumber
import json
import sys
import os
__friendly_name__ = "Get Antivirus Status"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_antivirus_status(device_id=None):
    # If device_id wasn't provided as an argument, ask for it
    if device_id is None:
        device_id = input("Enter device identifier: ")
    
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.devices(device_id).antivirus.get()
        
        print("\nAntivirus status information:")
        print(json.dumps(result, indent=4))
        
        # If you want to display specific status information for better readability
        if 'Data' in result:
            data = result['Data']
            print("\nStatus Summary:")
            print(f"Protection Status: {data.get('ProtectionStatus', 'unknown')}")
            print(f"Definitions Status: {data.get('DefinitionsStatus', 'unknown')}")
            print(f"Scan Status: {data.get('ScanStatus', 'unknown')}")
            print(f"Update Status: {data.get('UpdateStatus', 'unknown')}")
            print(f"Policy: {data.get('Policy', 'unknown')}")
            
            if 'AgentStatus' in data and data['AgentStatus']:
                print("Agent Status:", ", ".join(data['AgentStatus']))
            
    except Exception as e:
        print('\nGetAntivirusStatus raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_antivirus_status()
