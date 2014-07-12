import sys
from cinderclient.v1 import client
from credentials import get_cinder_credentials

credentials = get_cinder_credentials()
try:
    cinder_client = client.Client(*credentials, service_type="volume")
    vol_list = cinder_client.volumes.list()
    vol_del = sys.argv[1]
    vol_exists = False
    for v in vol_list:
        if v.display_name == vol_del:
            print "volume %s exists" % vol_del
            vol_exists = True
            break
    if not vol_exists:
        print "volume %s doesnot exist" % vol_del
    else:
        cinder_client.volumes.delete(v)
        print "deleting volume..............."
        print "volume %s deleted" % vol_del
finally:
    print "Execution completed"
