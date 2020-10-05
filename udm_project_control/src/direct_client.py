#!/usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from udm_project_control.srv import *


def move_client(joint0, joint1, joint2, group):
    #service_name = 'direct_kin_service_' + str(group.data)
    service_name = 'direct_kin_service_' + str(group)
    
    rospy.wait_for_service(service_name)
    try:
        direct_kin_service_call = rospy.ServiceProxy(service_name, direct_kin_service)
        resp1 = direct_kin_service_call(joint0, joint1, joint2)
        return resp1.message
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [joint0 joint1 joint2 group]"%sys.argv[0]

if __name__ == "__main__":

    steps = rospy.get_param('~steps',"10")
    print("steps:" + str(steps))

    counter = 0

    while counter <= steps:

        if (counter % 2):
        
            print("start moving leg1")

            joint0 = Float32(data=float(0))
            joint1 = Float32(data=float(-0.45))
            joint2 = Float32(data=float(1))
    
            move_client(joint0, joint1,joint2, 'leg1')
        
            print("start moving leg3")

            joint0 = Float32(data=float(0.5))
            joint1 = Float32(data=float(-0.15))
            joint2 = Float32(data=float(0.38))

            move_client(joint0, joint1,joint2, 'leg3')

            #back to initial position
            joint0 = Float32(data=float(0))
            joint1 = Float32(data=float(0))
            joint2 = Float32(data=float(0))
            
            move_client(joint0, joint1,joint2, 'leg4')
            move_client(joint0, joint1,joint2, 'leg2')

        else:
            print("start moving leg2")

            joint0 = Float32(data=float(0))
            joint1 = Float32(data=float(-0.45))
            joint2 = Float32(data=float(1))
    
            move_client(joint0, joint1,joint2, 'leg4')
        
            print("start moving leg4")

            joint0 = Float32(data=float(-0.5))
            joint1 = Float32(data=float(-0.15))
            joint2 = Float32(data=float(0.38))

            move_client(joint0, joint1,joint2, 'leg2')

            #back to initial position
            joint0 = Float32(data=float(0))
            joint1 = Float32(data=float(0))
            joint2 = Float32(data=float(0))

            move_client(joint0, joint1,joint2, 'leg1')
            move_client(joint0, joint1,joint2, 'leg3')


        counter = counter + 1
    


