"generate config for multiple vrids under an interface"

def gen_vrid(ip='1.1.1.1', prio=100, number=250, mode='slow', init_wait=0):
    for i in range(number):
        id = i+1+2
        print ' vrrp', id, 'backup'
        print '  v', ip[:-1] + str(id)
        if prio!=100: print '  prio', prio
        if mode=='fast': print '  ad mi 500'
        else: print '  ad 1'
        if init_wait: print '  init-wait', init_wait


print 'context', 'r1'
print 'in', 'p1'
print ' ip ad 1.1.1.1/24' 
 
#gen_vrid(mode='fast', prio=20)
gen_vrid(prio=20)
print 'context', 'r2'
print 'in', 'p2'
print ' ip ad 1.1.1.2/24'

gen_vrid()
    
    