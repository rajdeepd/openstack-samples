from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from utils import print_values_server
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

server_id = 'b7ab88a1-b2d5-49f5-aa3f-9bcd63e05f03'
network_id = '240ff9df-df35-43ae-9df5-27fae87f2492'
server_detail = nova_client.servers.get(server_id)
print server_detail.id
#server_list = servers['servers']

#for s in server_list:
#    print s['id']
if server_detail is not None:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    ports = neutron.list_ports()

    print print_values_server(ports, server_id, 'ports')
    body_value = {
        "port": {
        "admin_state_up": True,
        "device_id": server_id,
        "name": "port1",
        "network_id": network_id
        }
    }
    response = neutron.create_port(body=body_value)
    print response
