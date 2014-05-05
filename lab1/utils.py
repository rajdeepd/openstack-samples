

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

def print_server(s):
    print("----------------------------------")
    print("server id: %s" % s.id)
    print("server name: %s" % s.name)
    print("server image: %s" % s.image)
    print("server flavour: %s" % s.flavor)
    print("server key name: %s" % s.key_name)
    print("user_id: %s" % s.user_id)
    print("----------------------------------")

def print_values_ip(ip_list):
    ip_dict_lisl = []
    for i in ip_list:
        print("----------------------------------")
        print("fixed_ip : %s" % i.fixed_ip)
        print("id : %s" % i.id)
        print("instance_id : %s" % i.instance_id)
        print("ip : %s" % i.ip)
        print("pool : %s" % i.pool)

def print_flavors(flavor_list):
    for f in flavor_list:
       print("----------------------------------")
       print("flavor id : %s" % f.id)
       print("flavor name : %s" % f.name)
    print("----------------------------------")
