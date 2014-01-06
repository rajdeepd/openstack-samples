import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url
    #Looks like a potential bug
    #if keystone.auth_url != keystone.management_url:
    #    keystone.management_url = keystone.auth_url
    tenant_name = 'user3-project'
    tenant_exists = False

    tenants_list = keystone.tenants.list()
    for t in tenants_list:
        if t.name ==  tenant_name:
	    tenant_exists = True
    if tenant_exists :
        print 'Tenant %s exists.' % tenant_name
    else:
        print 'Creating tenant %s ' % tenant_name
        req_body = {
            "tenant": {
                "name": tenant_name,
                "description": "Tenant  user3-project",
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
