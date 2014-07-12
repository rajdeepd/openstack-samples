import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 3:
    print("Please provide the username and password  on command line")
    print("format : $python -m keystonesamples.create_user <username> <password>")
    sys.exit()

user_name = args[1]
password = args[2]
credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    #Please make sure tenant_id is valid
    tenant_id = '5bf0eff1975b48959412f537d427c66c'
    req_body = {
        "user": {
            "name": user_name,
            "password": password,
            "tenantId": tenant_id,
            "enabled": True,
            "email": None
        }
    }
    user_list = keystone.users.list()
    user_exists = False
    for u in user_list:
        if u.name == user_name:
            print "%s already exists" % u.name
            user_exists = True
            break
    if not(user_exists):
        user = keystone.users.create(req_body['user']['name'],
                                     req_body['user']['password'],
                                     email=req_body['user']['email'],
                                     tenant_id=req_body['user']['tenantId'],
                                     enabled=req_body['user']['enabled'])
        print "User created %s" % user
except Exception as e:
    print e
finally:
    print "Execution Completed."
