from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from utils import print_values_server
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

#replace with server_id and network_id from your environment

router_id = '72cf1682-60a8-4890-b0ed-6bad7d9f5466'
network_id = '81bf592a-9e3f-4f84-a839-ae87df188dc1'
try:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    router = neutron.show_router(router_id)
    print router
    body_value = {
        "port": {
        "admin_state_up": True,
        "device_id": router_id,
        "name": "port1",
        "network_id": network_id
        }
    }
    response = neutron.create_port(body=body_value)
    print response
finally:
    print "Execution Completed"
