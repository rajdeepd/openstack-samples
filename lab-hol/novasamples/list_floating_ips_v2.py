from credentials import get_nova_credentials_tenant
from novaclient.client import Client
from utils import print_values_ip

#credentials = get_nova_credentials_v2()
username = 'user1'
password = 'user1'
tenant_name = 'user1-project'
credentials = get_nova_credentials_tenant(username, password,
                                              tenant_name, '2')
nova_client = Client(**credentials)
ip_list = nova_client.floating_ips.list()
print_values_ip(ip_list)
