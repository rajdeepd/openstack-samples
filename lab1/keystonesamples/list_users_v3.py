import keystoneclient.v3.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url

    users_list = keystone.users.list()
    for u in users_list:
        print 'name : %s' % u.name
        print 'id : %s' % u.id
        if hasattr(u, 'tenantId'):
            print 'tenantId : %s' % u.tenantId
            print '\n'
finally:
    print "Execution Completed."
