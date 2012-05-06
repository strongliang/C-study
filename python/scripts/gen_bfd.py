def gen_bfd(n=255):
    print 'router bfd'
    for i in range(1, n+1):
        print '  interface p' + str(i)
        print '  minimum transmit-interval 100'
        print '  minimum receive-interval 100'
        print '  detection-multiplier 3'


def vrrp_no_bfd(ip='1.1.1.1', n=255):
    for i in range(1, n+1):
        print 'in p'+str(i)
        print '    vrrp', str(i), 'backup'
        print '    no bfd neighbor '+ip[:-3]+str(i)+'.'+ip[-1]
                
                

