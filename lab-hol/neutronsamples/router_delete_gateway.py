from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials_tenant_one
from credentials import get_nova_credentials
from credentials import get_credentials
import sys
from utils import get_router_id
from utils import get_network_id

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the vm name on the command line")
    print("format : $python -m neutronsamples.router_add_gateway <router_name>")
    sys.exit()

router_name = args[1]

try:
    neutron_credentials = get_credentials_tenant_one("admin", "admin_pass", "admin")
    credentials = get_credentials()
    neutron = client.Client(**neutron_credentials)

    router_id = get_router_id(neutron, router_name)
    print("router_id:" + router_id)
    
    response = neutron.remove_gateway_router(router_id)
    print(response)
finally:
    print "Execution Completed"
