import os
import novaclient
from credentials import get_nova_credentials_v3
from novaclient.v3 import client
from novaclient.client import Client
#from novaclient.v3 import servers


d = {}
d['version'] = '2'
d['username'] = os.environ['OS_USERNAME']
d['password'] = os.environ['OS_PASSWORD']
d['auth_url'] = os.environ['OS_AUTH_URL']
d['project_id'] = os.environ['OS_TENANT_NAME']

#cs = novaclient.v3.client.Client(d['username'],d['password'],d['project_id'],d['auth_url'])
cs = novaclient.v3.client.Client('admin','admin_pass','admin','http://192.168.0.13:35357/v2.0')
#credentials = get_nova_credentials_v3()
#nova_client = Client(**credentials)

print(cs.servers.list())
print cs
#print(nova_client.servers.list())
