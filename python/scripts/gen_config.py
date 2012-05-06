from gen_vrrp_intf import *
from gen_bfd import *
from gen_vlan import *


def vlan_vrrp(num):
#    print 'service mul'
#    print 'context r1'
#    gen_vrrp_intf(ip='1.1.1.1', mode='fast', n=num)
#    
##    print 'port ether 19/11'
#    print 'port ether 2/20'
#    print 'no shut'
#    gen_vrrp_vlan("r1", n=num)
    
    
    print 'context r2'
    gen_vrrp_intf(ip='1.1.1.2', mode='slow', n=num)    
    
#    print 'port ether 19/21'
    print 'port ether 19/20'
    print 'no shut'
    gen_vrrp_vlan("r2", n=num)

def bfd(num):
#    print 'context r1'
#    gen_bfd(n=num)
#    print 'end'
#    print 'config'
#    print 'context r1'
#    #gen_vrrp_intf(ip='1.1.1.1', mode='fast')
#    gen_vrrp_intf(ip='1.1.1.1', mode='slow', bfd='1.1.1.2', n=num)
    print 'context r2'
    gen_bfd(n=num)
    print 'end'
    print 'config'
    print 'context r1'
    #gen_vrrp_intf(ip='1.1.1.2', mode='fast')
    gen_vrrp_intf(ip='1.1.1.2', mode='slow', bfd='1.1.1.1', n=num)
    
    
def ulag(num):
#    print 'service mul'
    print 'context r1'
    gen_vrrp_intf(ip='1.1.1.1', mode='slow', n=num)
    
    print 'link-group lg1'
    gen_vrrp_vlan("r1", n=num)
    

#    print 'context r2'
#    gen_vrrp_intf(ip='1.1.1.2', mode='slow', n=num)    
#    
#    print 'link-group lg2'
#    gen_vrrp_vlan("r2", n=num)
    
#vlan_vrrp(255)
bfd(255)
#ulag(255)



