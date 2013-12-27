
def print_values(val,type):
    val_type = None
    if type=='ports':
         val_list = val['ports']
    
    if type=='networks':
         val_list = val['networks']
    #port_list = ports['ports']
    for p in val_list:
        for k,v in p.items():
    	    print "%s : %s" % (k, v)
        print '\n'    
