from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values


credentials = get_credentials()
neutron = client.Client(**credentials)
ports = neutron.list_ports()
print_values(ports, 'ports')
