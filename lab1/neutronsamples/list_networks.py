from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_networks


credentials = get_credentials()
neutron = client.Client(**credentials)
netw = neutron.list_networks()

print_networks(netw)
