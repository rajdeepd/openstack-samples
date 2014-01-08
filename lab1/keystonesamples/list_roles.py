import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials
from credentials import get_credentials_tenant

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    tenants_list = keystone.tenants.list()
    for t in tenants_list:
        print t.name
        credentials_tenant = get_credentials_tenant(t.name)
        try:
            keystone_tenant = ksclient.Client(**credentials_tenant)
            roles = keystone_tenant.roles.list()
            for r in roles:
                print r
        except Exception as inst:
	    print 'Exception %s' % inst
            break
finally:
    print "Execution Completed."
