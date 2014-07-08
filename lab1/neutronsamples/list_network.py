from neutronclient.v2_0 import client
from credentials import get_credentials_tenant_one
from utils import print_values

credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
neutron = client.Client(**credentials)
netw = neutron.list_networks()

print_values(netw, 'networks')
