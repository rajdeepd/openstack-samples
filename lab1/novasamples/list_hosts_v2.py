from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_hosts

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)
host_list = nova_client.hosts.list()

print_hosts(host_list)
