from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials_tenant_one
from credentials import get_nova_credentials
from utils import print_values_server

credentials = get_credentials_tenant_one('user1', 'user1', 'user1-project')
neutron = client.Client(**credentials)

body_value = {'router': {
    'name' : 'user2-router',
    'admin_state_up': True,
}}
#response = neutron.create_port(body=body_value)
router = neutron.create_router(body=body_value)
print(router)
print("Execution Completed")
