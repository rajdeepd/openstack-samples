import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

image = nova_client.images.find(name="cirros")
flavor = nova_client.flavors.find(name="m1.tiny")
instance = nova_client.servers.create(name="vm2", image=image, flavor=flavor, key_name="keypair")
print "Sleeping for 5s after create command"
time.sleep(5)
print "List of VMs"
print nova_client.servers.list()

