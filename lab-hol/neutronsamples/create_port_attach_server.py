from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

#replace with server_id and network_id from your environment

server_id = 'b7ab88a1-b2d5-49f5-aa3f-9bcd63e05f03'
network_id = '240ff9df-df35-43ae-9df5-27fae87f2492'
server_detail = nova_client.servers.get(server_id)
print server_detail.id

if server_detail is not None:
    credentials = get_credentials()
    neutron = client.Client(**credentials)

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
