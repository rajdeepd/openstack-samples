import time
from credentials import get_nova_credentials_tenant
from novaclient.client import Client

try:
    username = 'user1'
    password = 'user1'
    tenant_name = 'user1-project'
    vm_name = 'test3'
    credentials = get_nova_credentials_tenant(username, password, 
                                              tenant_name, '2')
    nova_client = Client(**credentials)

    image = nova_client.images.find(name="cirros")
    flavor = nova_client.flavors.find(name="m1.tiny")
    net_id = 'ae0618cf-fa34-4e8b-816d-c1356c409119'
    nic_d = [{'net-id': net_id}]
    instance = nova_client.servers.create(name=vm_name, image=image,
                                          flavor=flavor, key_name="keypair-1", 
                                          nics=nic_d)
    print("Sleeping for 5s after create command")
    time.sleep(5)
    print("VM Created")
    print("id: "+ instance.id)
    print("name: " + instance.name)
    #print("List of VMs")
    #print(nova_client.servers.list())
finally:
    print("Execution Completed")
