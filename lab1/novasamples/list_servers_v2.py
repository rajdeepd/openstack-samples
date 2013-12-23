from credentials import get_nova_credentials_v2
from novaclient.client import Client
#nova = Client(2, "admin", "admin_pass", "admin", "http://192.168.101.15:35357/v2.0")
credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

print nova_client.servers.list()

