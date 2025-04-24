import slumber
import config
import json
__friendly_name__ = "Get a Specific Device"
def get_specific_device(device_id):
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        
        # Use the specific device endpoint with the device_id
        result = api.devices(device_id).get()
        
        # Prettify the JSON output
        if 'Data' in result:
            print(json.dumps(result['Data'], indent=4))
        else:
            print(f"No data found for device with ID: {device_id}")
            print(json.dumps(result, indent=4))
            
    except Exception as e:
        print(f'Error retrieving device with ID {device_id}:')
        print(str(e))

if __name__ == "__main__":
    device_id = input("Enter device identifier: ")
    get_specific_device(device_id)
