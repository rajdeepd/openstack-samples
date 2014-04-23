from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

#replace with server_id and network_id from your environment

server_id = '9a52795a-a70d-49a8-a5d0-5b38d78bd12d'
network_id = 'ce5d204a-93f5-43ef-bd89-3ab99ad09a9a'
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
