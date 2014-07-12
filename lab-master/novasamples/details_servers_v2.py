from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

servers = nova_client.servers.list()

for s in servers:
    print("server id: %s" % s.id)
    print("server name: %s" % s.name)
    print("server image: %s" % s.image)
    print("server flavour: %s" % s.flavor)
    print("server key name: %s" % s.key_name)
    print("user_id: %s" % s.user_id)
    print("----------------------------------")
