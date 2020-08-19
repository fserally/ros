#!/usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from udm_hand_control.srv import *


def move_client(joint0, joint1, joint2, group):
    rospy.wait_for_service('move_service_fatimah')
    try:
        move_service_fatimah = rospy.ServiceProxy('move_service_fatimah', move_service)
        resp1 = move_service_fatimah(joint0, joint1, joint2,group)
        return resp1.message
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [joint0 joint1 joint2 group]"%sys.argv[0]

if __name__ == "__main__":
    joint0 = Float32(data=float(sys.argv[1]))
    joint1 = Float32(data=float(sys.argv[2]))
    joint2 = Float32(data=float(sys.argv[3]))
    group = String(data=sys.argv[4])
    move_client(joint0, joint1,joint2, group)
        

    
