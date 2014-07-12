from ceilometerclient import client
from credentials import get_ceilo_credentials

creds = get_ceilo_credentials()
ceilometer = client.get_client(api_version=2, **creds)
meters = ceilometer.meters.list()
for meter in meters:
    statistic = ceilometer.statistics.list(str(meter.name))
    print("%s: %s" % (str(meter.name), str(statistic)))
