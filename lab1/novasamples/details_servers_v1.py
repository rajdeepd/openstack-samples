
from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

#print nova_client.servers.list(detailed=T)

servers = nova_client.servers.list()

for s in servers:

    print "server name: %s \n" % s.name
    print "server image: %s \n" % s.image
    print "server flavour: %s \n" % s.flavor
    print "server key name: %s \n" % s.key_name
    print "server id: %s \n" % s.id
    print "user_id: %s \n" % s.user_id
