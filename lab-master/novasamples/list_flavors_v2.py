from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_flavors

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

flavors_list =  nova_client.flavors.list()

print_flavors(flavors_list)
