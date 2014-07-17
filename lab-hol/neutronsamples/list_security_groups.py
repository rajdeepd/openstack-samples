from neutronclient.v2_0 import client
from utils import print_values
from credentials import get_credentials_tenant_one

credentials = get_credentials_tenant_one("user1", "user1", "user1-project")
neutron = client.Client(**credentials)
sg = neutron.list_security_groups()
print sg
