openstack-samples
=================

###Getting Started

1.  Make sure you updated the script `openstack_env.sh` with appropriate values for the variables.

2.  Execute the script to setup the environment variables


```bash
source openstack_env.sh
```

###Nova

#### API v2

Initialize the Nova Client using the following code

```
credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)
```
List VMs using the following command

```
nova_client.servers.list()
```

Run the following command from `openstack/lab1` folder

```bash
python -m novasamples.list_servers_v2
```

###Keystone