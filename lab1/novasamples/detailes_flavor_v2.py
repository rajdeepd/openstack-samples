from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

flavors_list = nova_client.flavors.list()
flavor = "m1.tiny"
flavor_exists = False

for flav in flavors_list:
    if flav.name == flavor:
        print "flavor %s exists" % flavor
        flavor_exists = True
        break
if not flavor_exists:
    print "flavor %s doesnot exists" % flavor
else:
    print "flavor name:", flav.name
    print "flavor RAM:", flav.ram
    print "flavor vcpus:", flav.vcpus
    print "flavor disk:", flav.disk
    print "flavor id:", flav.id
    print "flavor ephemeral:", flav.ephemeral
    print "flavor factor:", flav.rxtx_factor
