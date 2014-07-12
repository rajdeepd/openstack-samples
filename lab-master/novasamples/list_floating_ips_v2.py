from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_values_ip

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)
ip_list = nova_client.floating_ips.list()
print_values_ip(ip_list)
