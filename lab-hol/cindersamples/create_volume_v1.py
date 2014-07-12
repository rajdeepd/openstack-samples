from cinderclient.v1 import client
from credentials import get_cinder_credentials

credentials = get_cinder_credentials()

try:
    cinder_client = client.Client(*credentials, service_type="volume")
    vol_list = cinder_client.volumes.list()

    vol_name = "voltest1"
    vol_type = "test"
    vol_size = 1
    vol_exists = False
    for v in vol_list:
        if v == vol_name:
            print "volume %s exists" % vol_name
            vol_exists = True

    if vol_exists == False:
        volume = cinder_client.volumes.create(1, display_name=vol_name,
                                             volume_type=vol_type)

        print volume

finally:
    print "Execution completed"
