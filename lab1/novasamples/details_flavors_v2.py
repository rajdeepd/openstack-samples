from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

flavors_list = nova_client.flavors.list()

for flav in flavors_list:
    print "flavor details: "
    print "name:", flav.name
    print "RAM:", flav.ram
    print "vcpus:", flav.vcpus
    print "disk:", flav.disk
    print "id:", flav.id
    print "ephemeral:", flav.ephemeral
    print "factor:", flav.rxtx_factor
    print "\n"
