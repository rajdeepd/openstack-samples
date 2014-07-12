import os
from cinderclient.v2 import client
from credentials import get_cinder_credentials

credentials = get_cinder_credentials()

try:
    cinder_client = client.Client(*credentials, service_type="volume")
    print cinder_client.volume_types.create("type1")

finally:
    print "Execution completed"
