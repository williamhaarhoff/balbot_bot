#!/usr/bin/env python 

import rospy 
import numpy as np 
from std_msgs.msg import Float64 
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Imu
import tf


class converter:
	def __init__(self):
		rospy.init_node('tilt_converter',anonymous=False)
		self.pub = rospy.Publisher('tilt',Float64,queue_size = 10)
		self.sub = rospy.Subscriber('imu_data',Vector3,self.callback)

		self.tilt = 0.0

	def callback(self,data):
		self.pub.publish(data.y)



if __name__=='__main__':
	conv = converter()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass


