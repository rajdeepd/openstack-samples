import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url
    #Looks like a potential bug
    if keystone.auth_url != keystone.management_url:
        keystone.management_url = keystone.auth_url

    role_name = "role1"
    role_exists = False
    roles = keystone.roles.list()
    for r in roles:
        if r.name == role_name:
            role_exists = True

    if role_exists:
        print "%s already exists" % role_name

    else:
        user_role = keystone.roles.create(role_name)
        print "Created role %s" % role_name
finally:
    print "Execution Completed ."
