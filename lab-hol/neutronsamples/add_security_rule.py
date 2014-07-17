from neutronclient.v2_0 import client
from utils import print_values
from credentials import get_credentials_tenant_one

sg_name = 'default'
credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
neutron = client.Client(**credentials)
sg = neutron.list_security_groups()
sg_list = sg['security_groups']
sg_id = ''
for sg in sg_list:
    if sg['name'] == sg_name:
        sg_id = sg['id']
        exit


body = {'security_group_rule':
           {'security_group_id': sg_id,
            'direction': 'ingress',
            'ethertype': 'ipv4',
            'protocol': 'icmp',
            'port_range_min': None,
            'port_range_max': None
           }
}
rule = neutron.create_security_group_rule(body)
