from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials_tenant_one
from credentials import get_nova_credentials
import sys
from utils import get_router_id
from utils import get_network_id

args = sys.argv
args_len = len(sys.argv)

if args_len != 4:
    print("Please provide the vm name on the command line")
    print("format : $python -m neutronsamples.create_port_attach_router <router_name> <network_name> <port_name>")
    sys.exit()

router_name = args[1]
network_name = args[2]
port_name = args[3]

try:
    nova_credentials = get_nova_credentials()
    nova_client = nvclient.Client(**nova_credentials)
    neutron_credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
    neutron = client.Client(**neutron_credentials)

    router_id = get_router_id(neutron, router_name)
    network_id = get_network_id(neutron, network_name)

    router = neutron.show_router(router_id)
    print router
    body_value = {
        "port": {
        "admin_state_up": True,
        "device_id": router_id,
        "name": port_name,
        "network_id": network_id
        }
    }
    response = neutron.create_port(body=body_value)
    print response
finally:
    print "Execution Completed"
