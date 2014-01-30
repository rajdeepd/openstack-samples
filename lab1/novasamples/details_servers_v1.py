
from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

#print nova_client.servers.list(detailed=T)

servers = nova_client.servers.list()

for s in servers:

    print "server name:\n", s.name
    print "server image:\n", s.image
    print "server flavour:\n", s.flavor
    print "server key name:\n", s.key_name
    print "server id:\n", s.id
