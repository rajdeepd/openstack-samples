import novaclient.v1_1.client as nvclient
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

servers =  nova_client.servers.list()

for(var s in servers)
    print s.id
    print s.name
    print s.flavor
    print s.net_id
 
