from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials
from utils import print_values_server

router_id = '72cf1682-60a8-4890-b0ed-6bad7d9f5466'
network_id = '240ff9df-df35-43ae-9df5-27fae87f2492'
credentials = get_credentials()
neutron = client.Client(**credentials)
router = neutron.show_router(router_id)
print(router)
body_value = {'port': {
'admin_state_up': True,
'device_id': router_id,
'name': 'port1',
'network_id': network_id,
}}
response = neutron.create_port(body=body_value)
print(response)
print("Execution Completed")
