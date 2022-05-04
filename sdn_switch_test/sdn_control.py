import os
import sys

def acl_deploy(dele):
    basic_command = 'python3 /home/hw/tmp_share/hxc/exp_control-master/exp_control-master/switch_control/acl_hw.py '
    paras = [['10.174.216.35', '192.168.6.3', '100GE1/0/10', '172.166.14.1', '510'],
             ['10.174.216.48', '192.168.6.3', '100GE1/0/30', '172.166.16.2', '511'],  
             ['10.174.216.48', '192.168.6.3', '100GE1/0/31', '172.166.16.2', '512'],
             ['10.174.216.35', '192.168.6.3', '100GE1/0/64', '192.168.8.3', '513']]
    delete = ''
    if(dele):
        delete = '--onlydel True'
    for para in paras:
        switchIp = '--switchIp ' + para[0] + ' '
        source = '--source ' + para[1] + ' '
        inport = '--inport ' + para[2] + ' '
        outport = '--outport ' + para[3] + ' '
        aclId = '--aclId ' + para[4] + ' '
        command = basic_command + switchIp + source + inport + outport + aclId + delete
        # print(command)
        os.system(command)



if __name__ == '__main__':
    acl_deploy(0)