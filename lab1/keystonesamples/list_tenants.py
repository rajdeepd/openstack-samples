import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url
    #Looks like a potential bug
    if keystone.auth_url != keystone.management_url:
        keystone.management_url = keystone.auth_url

    tenants_list = keystone.tenants.list()
    for t in tenants_list:
        print t

finally:
    print "Execution Completed."
