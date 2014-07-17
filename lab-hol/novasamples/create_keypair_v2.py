from credentials import get_nova_credentials_tenant
from novaclient.client import Client

credentials = get_nova_credentials_tenant('user1','user1', 
                                         'user1-project', '2')
nova_client = Client(**credentials)
name = 'keypair-2'
keypair = nova_client.keypairs.create(name)
print(keypair)


