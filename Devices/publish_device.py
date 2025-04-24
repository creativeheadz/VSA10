import slumber
import json
import sys
import os
__friendly_name__ = "Publish a Device"
# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_user_input(prompt, default):
    """Get user input with a default value."""
    user_input = input(f"{prompt} [{default}]: ")
    return user_input if user_input.strip() else default

def publish_device():
    # Default values
    default_instance_id = "00000000-0000-0000-0000-000000000000"
    default_name = "Production Web Site"
    default_group_id = 123
    default_description = "Running on ip.91.71.60.196.us-west-2.compute.internal"
    default_refresh = 5
    default_notify = "false"
    
    # Get user input with defaults
    print("\n=== Device Publication Details ===")
    instance_id = get_user_input("Enter Instance ID", default_instance_id)
    name = get_user_input("Enter Device Name", default_name)
    
    # For group_id, ensure it's an integer
    group_id_input = get_user_input("Enter Group ID", str(default_group_id))
    try:
        group_id = int(group_id_input)
    except ValueError:
        print(f"Invalid Group ID. Using default: {default_group_id}")
        group_id = default_group_id
    
    description = get_user_input("Enter Description", default_description)
    
    # For refresh interval, ensure it's an integer
    refresh_input = get_user_input("Enter Refresh Interval (minutes)", str(default_refresh))
    try:
        refresh = int(refresh_input)
    except ValueError:
        print(f"Invalid Refresh Interval. Using default: {default_refresh}")
        refresh = default_refresh
    
    notify = get_user_input("Notify When Offline (true/false)", default_notify)

    # Create device contents structure
    contents_item3 = {
        "Icon": "information",
        "Type": "label",
        "Title": "5 hours, 39 minutes",
        "Subtitle": "Uptime",
    }

    contents_item2 = {
        "CallbackUrl": "https://admin.revoproject.com/api.php?key=d41d8cd98&action=reset_config",
        "Type": "webhook_command",
        "Title": "Reload Configuration",
        "Subtitle": "Reads configuration from file",
    }

    contents_item = {
        "Name": "Status",
        "Contents": [contents_item2, contents_item3],
    }

    # Create the request body
    request_body = {
        "InstanceId": instance_id,
        "Name": name,
        "GroupId": group_id,
        "Description": description,
        "Contents": [contents_item],
        "NextRefreshIntervalMinutes": refresh,
        "NotifyWhenOffline": notify,
    }

    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        result = api.devices.post(request_body)
        print("\nDevice published successfully:")
        print(json.dumps(result, indent=4))
    except Exception as e:
        print('\nPublishDevice raised an exception:')
        print(str(e))

if __name__ == "__main__":
    publish_device()
