from neutronclient.v2_0 import client
from credentials import get_credentials_tenant_one
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the vm name on the command line")
    print("format : $python -m neutronsamples.delete_network <network_name>")
    sys.exit()

network_name = args[1]
credentials = get_credentials_tenant_one("user1", "user1", "user1-project")

neutron = client.Client(**credentials)
try:
    networks = neutron.list_networks()['networks']
    network_exists = False
    for n in networks:
        if n["name"] == network_name:
            neutron.delete_network(n["id"])
            print("Deleted network id:%s , name: %s" % (n["id"], n["name"]))
            network_exists = True
    if not(network_exists):
        print("Network %s not found" % network_name)
finally:
    print "Execution completed"
