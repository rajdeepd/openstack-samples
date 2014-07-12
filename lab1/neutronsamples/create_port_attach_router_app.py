from neutronclient.v2_0 import client
from credentials import get_credentials_tenant_one
from utils import print_values_server


#replace with server_id and network_id from your environment

router_id = '92ed3287-5b40-4d09-8757-f3d9396e0f32'
network_id = '80808deb-6a6b-40d4-87f0-6ce80bbc7be0'
try:
    credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
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
