import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

image = nova_client.images.find(name="cirros")
flavor = nova_client.flavors.find(name="m1.tiny")
instance = nova_client.servers.create(name="vm1", image=image, flavor=flavor, key_name="keypair")

# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print "status: %s" % status
print nova_client.servers.list()

