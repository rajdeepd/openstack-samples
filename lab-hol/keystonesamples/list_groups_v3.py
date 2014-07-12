import keystoneclient.v3.client as ksclient
from credentials import get_credentials
import inspect

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    group = keystone.groups.list(user="55ace085f8494aaca33fb1da58c1fae3")
    print group
    #for g in groups_list:
        #print g
        #print 'name : %s' % u.name
        #print 'id : %s' % u.id
        #if hasattr(u, 'tenantId'):
        #    print 'tenantId : %s' % u.tenantId
        #print '\n'
finally:
    print "Execution Completed."
