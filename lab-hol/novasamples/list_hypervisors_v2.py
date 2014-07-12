from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_values_hypervisor

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

hyp_list = nova_client.hypervisors.list()

print_values_hypervisor(hyp_list)
