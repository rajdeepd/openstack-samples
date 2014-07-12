import sys
import os
from cinderclient.v2 import client
from credentials import get_cinder_credentials

credentials = get_cinder_credentials()
try:
    cinder_client = client.Client(*credentials, service_type="volume")
    vol_list = cinder_client.volumes.list()

    vol_name = sys.argv[1]
    vol_type = sys.argv[2]
    vol_size = sys.argv[3]
    vol_exists = False
    for v in vol_list:
        if v == vol_name:
            print "volume %s exists" % vol_name
            vol_exists = True
    if vol_exists == False:
        volume = cinder_client.volumes.create(vol_size, name=vol_name,
                 volume_type=vol_type)
        print volume
finally:
    print "Execution completed"
