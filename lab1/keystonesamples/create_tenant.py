import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the tenant name on command line")
    sys.exit() 

tenant_name =  args[1]
credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    tenant_exists = False

    tenants_list = keystone.tenants.list()
    for t in tenants_list:
        if t.name == tenant_name:
            tenant_exists = True
    if tenant_exists:
        print('Tenant %s exists.' % tenant_name)
    else:
        print('Creating tenant %s ' % tenant_name)
        req_body = {
            "tenant": {
                "name": tenant_name,
                "description": "Tenant: " + tenant_name,
                "enabled": True,
                "extravalue01": "metadata01",
            },
        }
        tenant = keystone.tenants.create(
            req_body['tenant']['name'],
            req_body['tenant']['description'],
            req_body['tenant']['enabled'])
        print tenant

finally:
    print "Execution Completed."
