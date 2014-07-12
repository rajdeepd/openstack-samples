from credentials import get_nova_credentials_tenant
from novaclient.client import Client
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the vm name on the command line")
    print("format : $python -m novasamples.delete_server_v2 <vm_name>")
    sys.exit()

vm_name = args[1]

username = 'user1'
password = 'user1'
tenant_name = 'user1-project'

credentials = get_nova_credentials_tenant(username, password,
                                              tenant_name, '2')

nova_client = Client(**credentials)

servers_list = nova_client.servers.list()
server_del = "test2"
server_exists = False

for s in servers_list:
    if s.name == server_del:
        print("This server %s exists" % server_del)
        server_exists = True
        break
if not server_exists:
    print("server %s does not exist" % server_del)
else:
    print("deleting server..........")
    nova_client.servers.delete(s)
    print("server %s deleted" % server_del)
