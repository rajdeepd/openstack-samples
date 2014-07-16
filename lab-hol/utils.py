

def print_values(val, type):
    val_type = None
    if type == 'ports':
        val_list = val['ports']
    if type == 'networks':
        val_list = val['networks']
    if type == 'routers':
        val_list = val['routers']
    if type == 'hypervisors':
        val_list = val
    for p in val_list:
        for k, v in p.items():
            print("%s : %s" % (k, v))
        print('\n')


def print_values_server(val, server_id, type):
    val_type = None
    if type == 'ports':
        val_list = val['ports']

    if type == 'networks':
        val_list = val['networks']
    for p in val_list:
        bool = False
        for k, v in p.items():
            if k == 'device_id' and v == server_id:
                bool = True
        if bool:
            for k, v in p.items():
                print("%s : %s" % (k, v))
            print('\n')


def print_values_hypervisor(hyp_list):
    hyp_dict_list = []
    for h in hyp_list:
        hyp = {}
        hyp['id'] = h.id
        hyp['vcpus'] = h.vcpus
        hyp['local_gb'] = h.local_gb
        hyp['hypervisor_type'] = h.hypervisor_type
        hyp['hypervisor_version'] = h.hypervisor_version
        hyp['free_ram_mb'] = h.free_ram_mb
        hyp['free_disk_gb'] = h.free_disk_gb
        hyp['current_workload'] = h.current_workload
        hyp['running_vms'] = h.running_vms
        hyp['cpu_info'] = h.cpu_info
        hyp['disk_available_least'] = h.disk_available_least
        hyp_dict_list.append(hyp)
    print(hyp_dict_list)


def print_values_img(img_list):
    img_dict_list = []
    for i in img_list:
        img = {}
        img['id'] = i.id
        img['name'] = i.name
        img['created'] = i.created
        img['minDisk'] = i.minDisk
        img['minRam'] = i.minRam
        img['progress'] = i.progress
        img['status'] = i.status
        img['updated'] = i.updated
        img['metadata'] = i.metadata
        img_dict_list.append(img)
    print(img_dict_list)

def print_server(server):
    print("-"*35)
    print("server id: %(id)s" % server)
    print("server name: %s" % server.name)
    print("server image: %s" % server.image)
    print("server flavour: %s" % server.flavor)
    print("server key name: %s" % server.key_name)
    print("user_id: %s" % server.user_id)
    print("-"*35)

def print_values_ip(ip_list):
    ip_dict_lisl = []
    for ip in ip_list:
        print("-"*35)
        print("fixed_ip : %s" % ip.fixed_ip)
        print("id : %s" % ip.id)
        print("instance_id : %s" % ip.instance_id)
        print("ip : %s" % ip.ip)
        print("pool : %s" % ip.pool)

def print_flavors(flavor_list):
    for f in flavor_list:
       print("----------------------------------")
       print("flavor id : %s" % f.id)
       print("flavor name : %s" % f.name)
    print("----------------------------------")

def print_hosts(host_list):
    for h in host_list:
       print("----------------------------------")
       print("host_name : %s" % h.host_name)
       print("service : %s" % h.service)
       print("zone : %s" % h.zone)
    print("----------------------------------")

def check_vm_name(nova_client, name):
    servers = nova_client.servers.list()
    server_exists = False
    for s in servers:
        if s.name == name:
            server_exists = True
            break
    return server_exists

def get_vm_id(nova_client, name):
    servers = nova_client.servers.list()
    ids = []
    for s in servers:
        if s.name == name:
            ids.append(s.id)
    return ids

def get_router_id(neutron_client, router_name):
    routers = neutron_client.list_routers()['routers']
    id  = ''
    for r in routers:
        if r['name'] == router_name:
            id = r['id']
            break
    return id

def get_network_id(neutron_client, network_name):
    networks = neutron_client.list_networks()['networks']
    id  = ''
    for n in networks:
        if n['name'] == network_name:
            id = n['id']
            break
    return id

def get_subnet_id(neutron_client, subnet_name):
    subnets = neutron_client.list_subnets()['subnets']
    id = ''
    for s in subnets:
        if s['name'] == subnet_name:
            id = s['id']
            break
    return id
