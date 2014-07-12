from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_server

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

# Change the server_id specific to your environment

server_id = '99889c8d-113f-4a7e-970c-77f1916bfe14'
server = nova_client.servers.get(server_id)
n = server.name
print_server(server)

server.update(name = n + '1')
server_updated = nova_client.servers.get(server_id)
print_server(server_updated)


