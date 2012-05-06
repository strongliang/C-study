def gen_vrrp_intf(ip='1.1.1.1', n=255, mode='fast', bfd=''):
    for i in range(1, n+1):
        print 'in p'+str(i)
        intf_ip = ip[:-3]+str(i)+'.'+ip[-1] + '/24'
        print '  ip add ' + intf_ip
        print '    vrrp', str(i), 'backup'
        print '    v', ip[:-3]+str(i)+'.'+'100'
        if mode=='fast': print '    ad mi 100'
        else: print '    ad 1'
        if bfd: print '    bfd neighbor '+ ip[:-3]+str(i)+'.'+bfd[-1]
        
        
        
#gen_vrrp_intf(n=3)



        
       
        