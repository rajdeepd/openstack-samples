from ceilometerclient import client
from credentials import get_ceilo_credentials

creds = get_ceilo_credentials()
ceilometer = client.get_client(api_version=2, **creds)

print ceilometer.meters.list()
