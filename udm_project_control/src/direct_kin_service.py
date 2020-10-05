#!/usr/bin/env python

from udm_project_control.srv import *
import rospy
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped

class groupService:

	def __init__(self):
		rospy.init_node('spider_service_server')
		self.group_name = rospy.get_param('~groupName',"leg1")
		print self.group_name
		print("service called")
		moveit_commander.roscpp_initialize(sys.argv)

		self.robot=moveit_commander.RobotCommander()
		self.scene =moveit_commander.PlanningSceneInterface()
		self.move_group =moveit_commander.MoveGroupCommander(self.group_name)
		display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory,queue_size=20)
    	# We can get the name of the reference frame for this robot:
		planning_frame = self.move_group.get_planning_frame()
		print "============ Planning frame: %s" % planning_frame

		# We can also print the name of the end-effector link for this group:
		eef_link = self.move_group.get_end_effector_link()
		print "============ End effector link: %s" % eef_link

		# We can get a list of all the groups in the robot:
		group_names = self.robot.get_group_names()
		print "============ Available Planning Groups:", self.robot.get_group_names()

		# Sometimes for debugging it is useful to print the entire state of the
		# robot:
		print "============ Printing robot state"
		print self.robot.get_current_state()
		print ""
		
		rospy.Service('direct_kin_service_%s'%(self.group_name), direct_kin_service, self.handle_req)
		rospy.spin()


	def handle_req(self,req):
		try:
			print req
			
			joint_goal = self.move_group.get_current_joint_values()
			joint_goal[0] = req.joint0.data
			joint_goal[1] = req.joint1.data
			joint_goal[2] = req.joint2.data
			self.move_group.set_joint_value_target(joint_goal)
			plan2 = self.move_group.plan()
			
			self.move_group.go(wait=True)
			self.move_group.stop()
			self.move_group.clear_pose_targets()
	
			rep=direct_kin_serviceResponse()
			rep.res.data=True
			rep.message.data="Success"
			return rep
		except Exception as e:
			rep=direct_kin_serviceResponse()
			print e
			return rep

if __name__ == "__main__":
	groupService()
