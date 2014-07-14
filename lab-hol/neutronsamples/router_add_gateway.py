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

if args_len != 3:
    print("Please provide the vm name on the command line")
    print("format : $python -m neutronsamples.router_add_gateway <router_name> <network_name>")
    sys.exit()

router_name = args[1]
network_name = args[2]

try:
    neutron_credentials = get_credentials_tenant_one("admin", "admin_pass", "admin")
    credentials = get_credentials()
    neutron = client.Client(**neutron_credentials)

    router_id = get_router_id(neutron, router_name)
    network_id = get_network_id(neutron, network_name)
    print router_id
    print network_id
    
    router_dict = {
        'network_id' : network_id,
        'enable_snat' :  True
    }
    neutron.add_gateway_router(router_id, router_dict)
finally:
    print "Execution Completed"
