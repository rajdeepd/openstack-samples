import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url
    #Looks like a potential bug
    if keystone.auth_url != keystone.management_url:
        keystone.management_url = keystone.auth_url

    req_body = {
            "tenant": {
                "name": "tenantX",
                "description": "Like tenant 9, but better.",
                "enabled": True,
                "extravalue01": "metadata01",
            },
    }
    tenant = keystone.tenants.create(
            req_body['tenant']['name'],
            req_body['tenant']['description'],
            req_body['tenant']['enabled']
            )
    print tenant

finally:
    print "Execution Completed."
