# get_all_devices.py
import slumber
import config
import json
__friendly_name__ = "Get all Devices"
def get_all_devices():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.devices.get(top='100', skip='0')  # Adjusted the arguments
        # Prettify the JSON output
        print(json.dumps(result, indent=4))
    except Exception as e:
        print('GetDevices raised an exception.')
        print(str(e))

if __name__ == "__main__":
    get_all_devices()
