from neutronclient.v2_0 import client
from novaclient.client import Client
from utils import print_values_server
from utils import get_vm_id
from credentials import get_nova_credentials_tenant
from credentials import get_credentials_tenant_one
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the vm name on the command line")
    print("format : $python -m novasamples.list_ports_server <vm_name>")
    sys.exit()

server_name = args[1]
username = 'user1'
password = 'user1'
tenant_name = 'user1-project'
credentials = get_nova_credentials_tenant(username, password, 
                                              tenant_name, '2')
nova_client = Client(**credentials)

server_id_list = get_vm_id(nova_client, server_name)
if len(server_id_list) > 1:
    raise Exception("More than one vm found")
    exit(3)
else:
    server_id = server_id_list[0]
    neutron_credentials = get_credentials_tenant_one(username, password, tenant_name)
    neutron = client.Client(**neutron_credentials)
    ports = neutron.list_ports()

    print print_values_server(ports, server_id, 'ports')
