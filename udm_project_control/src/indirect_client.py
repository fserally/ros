#!/usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from udm_project_control.srv import *


def move_client(x, y, z, group):
    #service_name = 'direct_kin_service_' + str(group.data)
    service_name = 'indirect_kin_service_' + str(group)
    
    rospy.wait_for_service(service_name)
    try:
        indirect_kin_service_call = rospy.ServiceProxy(service_name, indirect_kin_service)
        resp1 = indirect_kin_service_call(x, y, z)
        return resp1.message
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y z group]"%sys.argv[0]

if __name__ == "__main__":

    steps = rospy.get_param('~steps',"10")
    print("steps:" + str(steps))

    x = Float32(data=float(0))
    y = Float32(data=float(0))
    z = Float32(data=float(0.5))

    move_client(x, y,z, 'leg1')
    


