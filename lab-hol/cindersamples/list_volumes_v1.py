from cinderclient.v1 import client
from credentials import get_cinder_credentials

credentials = get_cinder_credentials()
try:
    cinder_client = client.Client(*credentials, service_type="volume")
    vol_list = cinder_client.volumes.list()
    for v in vol_list:
        print v.display_name
finally:
    print "Execution Completed"
