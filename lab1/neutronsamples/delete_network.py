from neutronclient.v2_0 import client
from credentials import get_credentials

network_name = "temp_network"
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
                "cidr": "192.168.199.0/24",
                "ip_version": 4,
                "network_id": network_id
            }
                ]
    }

    subnet = neutron.create_subnet(body=body_create_subnet)
    print "Created subnet %s" % subnet
    
    neutron.delete_network(network_id)
    print "Deleted Network %s" %network_id
finally:
    print "Execution completed"
