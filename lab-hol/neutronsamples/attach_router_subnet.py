from neutronclient.v2_0 import client
from credentials import get_credentials_tenant_one
import sys
from utils import get_router_id
from utils import get_subnet_id

args = sys.argv
args_len = len(sys.argv)

if args_len != 3:
    print("Please provide parameters on the command line")
    print("format : $python -m neutronsamples.attach_router_subnet <router_name> <subnet_name>")
    sys.exit()

router_name = args[1]
subnet_name = args[2]

try:
    neutron_credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
    neutron = client.Client(**neutron_credentials)

    router_id = get_router_id(neutron, router_name)
    subnet_id = get_subnet_id(neutron, subnet_name)
    body = {}
    body['subnet_id'] = subnet_id 
    neutron.add_interface_router(router_id, body)
finally:
    print "Execution Completed"
