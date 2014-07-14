from neutronclient.v2_0 import client
from credentials import get_credentials_tenant_one
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 3:
    print("Please provide the vm name on the command line")
    print("format : $python -m neutronsamples.create_network_tenant <network_name>i <cidr>")
    sys.exit()

network_name = args[1]
cidr = args[2]

subnet_name = network_name 
credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
neutron = client.Client(**credentials)
try:
    body_sample = {
        "network":
        {
            "name": network_name,
            "admin_state_up": True,
        }
    }
    netw = neutron.create_network(body=body_sample)
    net_dict = netw['network']
    network_id = net_dict['id']
    print "Network %s created" % network_id

    body_create_subnet = {
        "subnets": [
            {
                "name": subnet_name,
                "cidr": cidr,
                "ip_version": 4,
                "network_id": network_id
            }
        ]
    }

    subnet = neutron.create_subnet(body=body_create_subnet)
    print "Created subnet %s" % subnet
finally:
    print "Execution completed"
