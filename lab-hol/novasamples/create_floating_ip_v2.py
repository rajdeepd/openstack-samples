from credentials import get_nova_credentials_tenant
from credentials import get_credentials_tenant_one
from novaclient.client import Client
from neutronclient.v2_0 import client

credentials = get_nova_credentials_tenant('user1','user1', 
                                         'user1-project', '2')
nova_client = Client(**credentials)
s = nova_client.servers.find(name='app_vm')
print s.id

credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
neutron = client.Client(**credentials)
body = {'floatingip': {'floating_network_id': 'ffb0f959-847c-4486-9278-b5c89d710a76'}}
fip_id = 'ad37e825-34ea-4efe-b9ce-bce947e6d277'
update_dict = {'port_id' :'41c802c2-da79-4a98-8f1f-d2e324b405e2'}
response = neutron.update_floatingip(fip_id, {'floatingip':update_dict})
print("Updation response: %s" %response)

