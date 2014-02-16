import keystoneclient.v2_0.client as ksclient
from credentials import get_credentials

credentials = get_credentials()
try:
    keystone = ksclient.Client(**credentials)
    print keystone.auth_url

    users_list = keystone.users.list()
    for u in users_list:
        print u

finally:
    print "Execution Completed."
