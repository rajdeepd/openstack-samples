import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    tenants_list = keystone.tenants.list()
    for t in tenants_list:
        print t
finally:
    print "Execution Completed."
