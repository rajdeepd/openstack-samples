import time
from credentials import get_nova_credentials_v2
from novaclient.client import Client

try:
    credentials = get_nova_credentials_v2()
    nova_client = Client(**credentials)

    image = nova_client.images.find(name="cirros")
    flavor = nova_client.flavors.find(name="m1.tiny")
    #net_id = '81bf592a-9e3f-4f84-a839-ae87df188dc1'
    net_id = 'd05a7729-4bcf-4149-9d8f-6a4764520a04'
    nic_d = [{'net-id': net_id}]
    instance = nova_client.servers.create(name="vm2", image=image,
                                      flavor=flavor, key_name="keypair-1", nics=nic_d)
    print "Sleeping for 5s after create command"
    time.sleep(5)
    print "List of VMs"
    print nova_client.servers.list()
finally:
    print "Execution Completed"
