from credentials import get_nova_credentials_v11
from novaclient.client import Client

credentials = get_nova_credentials_v11()
nova_client = Client(**credentials)

print nova_client.servers.list()
