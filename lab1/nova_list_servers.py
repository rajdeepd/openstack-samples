import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials
# VERSION = "1.1"
# USERNAME = "admin"
# PASSWORD = "admin_pass"
#
# AUTH_URL = "http://183.83.27.73:27999/v2.0"
# PROJECT_ID = "admin"


credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)
#
# novaClient = nvclient.Client(USERNAME, PASSWORD,PROJECT_ID, auth_url=AUTH_URL,
#                   insecure=False, timeout=None, proxy_tenant_id=None,
#                   proxy_token=None, region_name=None,
#                   endpoint_type='publicURL', extensions=None,
#                   service_type='compute', service_name=None,
#                   volume_service_name=None, timings=False,
#                   bypass_url=None, os_cache=False, no_cache=True,
#                   http_log_debug=False, auth_system='keystone',
#                   auth_plugin=None,
#                   cacert=None)

print nova_client.servers.list()

