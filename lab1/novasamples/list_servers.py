import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

print nova_client.servers.list()

