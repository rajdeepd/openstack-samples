from credentials import get_nova_credentials_tenant
from novaclient.client import Client

username = 'user1'
password = 'user1'
tenant_name = 'user1-project'

credentials = get_nova_credentials_tenant(username, password, tenant_name, '2')
nova_client = Client(**credentials)

servers = nova_client.servers.list()

for s in servers:
    print("-"*35)
    print('id:        ' + s.id)
    print('name:      ' + s.name)
    print('flavor:    ' + str(s.flavor['id']))
    print('hostId:    ' + s.hostId)
    print('created:   ' + s.created)
    print('tenant_id: ' + s.tenant_id)
    print('status:    ' + s.status)

