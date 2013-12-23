from neutronclient.v2_0 import client

USER="admin"
PASS="admin_pass"
TENANT_NAME = "admin"
KEYSTONE_URL="http://192.168.101.15:35357/v2.0"


neutron = client.Client(username=USER,
                                password=PASS,
                                tenant_name=TENANT_NAME,
                                auth_url=KEYSTONE_URL)

nets = neutron.list_networks()