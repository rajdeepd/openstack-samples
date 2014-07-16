from credentials import get_nova_credentials_tenant
from credentials import get_credentials_tenant_one
from novaclient.client import Client
from neutronclient.v2_0 import client
from utils import get_network_id
import sys

args = sys.argv
args_len = len(sys.argv)

if args_len != 3:
    print("Please provide the vm name on the command line")
    print("format : $python -m novasamples.create_associate_floating_ip_v2 <vm_name> <network_name>")
    sys.exit()

vm_name = args[1]
net_name = args[2]

username = 'user1'
password = 'user1'
tenant_name = 'user1-project'
credentials = get_nova_credentials_tenant(username, password, 
                                          tenant_name, '2')
nova_client = Client(**credentials)
s = nova_client.servers.find(name='app_vm')
print("server id: %s" % s.id)

neutron_credentials = get_credentials_tenant_one(username, password, tenant_name)
neutron = client.Client(**neutron_credentials)
network_id = get_network_id(neutron, net_name)

body = {'floatingip': {'floating_network_id': network_id}}
fip = neutron.create_floatingip(body)
print("FloatingIP: %s" +  str(fip))

fip_id = fip['floatingip']['id']

neutron_credentials = get_credentials_tenant_one(username, password, tenant_name)
neutron = client.Client(**neutron_credentials)
ports = neutron.list_ports()['ports']
port_id = ''

for p in ports:
    if p['device_id'] == s.id:
        port_id = p['id']
        exit
if port_id != '':
    update_dict = {'port_id' : port_id}
    response = neutron.update_floatingip(fip_id, {'floatingip':update_dict})
    print("Updation response: %s" %response)
else:
    print("Port for server %s not found" % s.name)

