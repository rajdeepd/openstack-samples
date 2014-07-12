from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values

try:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    routers_list = neutron.list_routers(retrieve_all=True)
    print_values(routers_list, 'routers')
finally:
    print 'Execution Completed'
