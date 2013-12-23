#import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials
from novaclient.client import Client
nova = Client(2, "admin", "admin_pass", "admin", "http://192.168.101.15:35357/v2.0")
#credentials = get_nova_credentials()
#nova_client = nvclient.Client(**credentials)

print nova.servers.list()

