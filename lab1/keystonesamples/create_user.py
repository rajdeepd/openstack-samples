import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    user_name = "test-user"
    keystone = ksclient.Client(**credentials)
    #Please make sure tenant_id is valid
    tenant_id = 'e32aa814fe95471db493d7fcfc818583'
    req_body = {
        "user": {
            "name": user_name,
            "password": "test-user",
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
    if not(user_exists) :
        user = keystone.users.create(req_body['user']['name'],
                                     req_body['user']['password'],
                                     email=req_body['user']['email'],
                                     tenant_id=req_body['user']['tenantId'],
                                     enabled=req_body['user']['enabled'])
        print "User created %s" % user
finally:
    print "Execution Completed."
