
def print_networks(netw):
    net_dict = netw['networks']
    print'------------------------------------------------------'
    for n in net_dict:
        print 'name                   : %s' % n['name']
        print 'id                     : %s' % n['id']
        print 'subnets                : %s' % n['subnets']
        print 'status                 : %s' % n['status']
        print 'tenant_id              : %s' % n['tenant_id']
        print 'provider:network_type  : %s' % n['provider:network_type']
        print'------------------------------------------------------'
