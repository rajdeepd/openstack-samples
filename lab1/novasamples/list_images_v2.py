from credentials import get_nova_credentials_v2
from novaclient.client import Client
from utils import print_values_img

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

img_list = nova_client.images.list(detailed=True)
print_values_img(img_list)
