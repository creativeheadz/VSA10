import slumber
import json
import sys
import os

__friendly_name__ = "Get All Audit Log Entries"


# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_all_audit_logs():
    try:
        api = slumber.API(config.ENDPOINT, auth=(config.TOKEN_ID, config.TOKEN_SECRET))
        # use $top & $skip parameters
        params = {'top': '50', 'skip': '0'}
        result = api.auditlogs.get(**params)
        
        print("\nAudit logs:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        print('\nGetAuditLogs raised an exception:')
        print(str(e))

if __name__ == "__main__":
    get_all_audit_logs()
