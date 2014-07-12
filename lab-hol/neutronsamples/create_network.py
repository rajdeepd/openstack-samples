from neutronclient.v2_0 import client
from credentials import get_credentials

network_name = "user1-app-network"
credentials = get_credentials()
neutron = client.Client(**credentials)
try:
    body_sample = {
        "network":
        {
            "name": network_name,
            "admin_state_up": True
        }
                }
    netw = neutron.create_network(body=body_sample)
    net_dict = netw['network']
    network_id = net_dict['id']
    print "Network %s created" % network_id

    body_create_subnet = {
        "subnets": [
            {
                "cidr": "10.1.0.0/24",
                "ip_version": 4,
                "network_id": network_id
            }
                ]
    }

    subnet = neutron.create_subnet(body=body_create_subnet)
    print "Created subnet %s" % subnet
finally:
    print "Execution completed"
