#!/usr/bin/env python 

import rospy 
import numpy as np 
from std_msgs.msg import Float64




class splitter:
	def __init__(self):
		rospy.init_node('splitter',anonymous=False)
		self.publ = rospy.Publisher('/leftWheelCmdVel',Float64,queue_size = 10)
		self.pubr = rospy.Publisher('/rightWheelCmdVel',Float64,queue_size = 10)
		self.sub = rospy.Subscriber('/tilt_effort',Float64,self.callback)



	def callback(self,data):
		
		data.data = data.data
		self.publ.publish(data)
		self.pubr.publish(data)



if __name__=='__main__':
	conv = splitter()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
