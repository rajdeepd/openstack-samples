from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)
host_list = nova_client.hosts.list()

for h in host_list:
    print(h)
