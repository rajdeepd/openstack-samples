import time
from credentials import get_nova_credentials_tenant
from novaclient.client import Client
from utils import check_vm_name
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 2:
    print("Please provide the vm name on the command line")
    print("format : $python -m novasamples.create_server_v2 <vm_name>")
    sys.exit()

vm_name = args[1]

try:
    username = 'user1'
    password = 'user1'
    tenant_name = 'user1-project'
    
    credentials = get_nova_credentials_tenant(username, password, 
                                              tenant_name, '2')
    nova_client = Client(**credentials)
    server_exists = check_vm_name(nova_client, vm_name)
    if server_exists:
        print("Server with name %s already exists" % vm_name)
    else:
        image = nova_client.images.find(name="cirros")
        flavor = nova_client.flavors.find(name="m1.tiny")
        net_id = 'cd99c968-1213-45b5-9de2-240d97e73880'
        nic_d = [{'net-id': net_id}]
        instance = nova_client.servers.create(name=vm_name, image=image,
                                              flavor=flavor, key_name="keypair-1", 
                                              nics=nic_d)
        print("Sleeping for 5s after create command")
        time.sleep(5)
        print("VM Created")
        print("id: "+ instance.id)
        print("name: " + instance.name)
finally:
    print("Execution Completed")

