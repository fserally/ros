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



class groupService:

	def __init__(self):
		rospy.init_node('spider_indirect_service_server')
		self.group_name = rospy.get_param('~groupName',"ee1")
		print self.group_name
		print("service called")
		moveit_commander.roscpp_initialize(sys.argv)

		self.robot=moveit_commander.RobotCommander()
		self.scene =moveit_commander.PlanningSceneInterface()
		self.move_group =moveit_commander.MoveGroupCommander(self.group_name)
		display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory,queue_size=20)
		
		rospy.Service('indirect_kin_service_%s'%(self.group_name), indirect_kin_service, self.handle_req)
		rospy.spin()


	def handle_req(self,req):
		try:
			pose_goal = geometry_msgs.msg.Pose()
			pose_goal.orientation.w = 1.0
			pose_goal.position.x = req.x.data
			pose_goal.position.y = req.y.data
			pose_goal.position.z = req.z.data
			
			self.move_group.set_pose_target(pose_goal)
			self.move_group.go(wait=True)
			self.move_group.stop()
			self.move_group.clear_pose_targets()

			rep=indirect_kin_serviceResponse()
			rep.res.data=True
			rep.message.data="Success"
			return rep

		except Exception as e:
			rep=direct_kin_serviceResponse()
			rep.message.data=e
			return rep

if __name__ == "__main__":
	groupService()
