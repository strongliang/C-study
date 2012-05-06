def gen_vrrp_vlan(context, n=255):
    print 'enc dot1q'
    for i in range(1, n+1):
        print '  dot1q pvc ' + str(i) + '0' 
        print '  bind in p' + str(i), context
        
        
        
