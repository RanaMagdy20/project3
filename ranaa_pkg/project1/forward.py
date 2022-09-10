#!/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import math 
import time
import numpy as np

x=0
Y=0
w=0
duration=0
vel=0
dlta=0
beta=0
def poseback (posemsg:Pose):
    global x 
    global y, w
    x=posemsg.x
    y=posemsg.y
    w=posemsg.theta

def move(timee,vel,dlta):
   
    
    vel_msg = Twist()
  
    while (True) :
        Delta=np.tan(dlta)
        beta=np.arctan((CGtoBack*Delta)/(CGtoFront+CGtoBack))
      
        vel_msg.linear.x=vel*np.cos(w+beta)
        vel_msg.linear.y=vel*np.sin(w+beta)
        vel_msg.linear.z=0 
    
        vel_msg.angular.z=((vel*np.cos(beta)*Delta)*(1/( CGtoBack + CGtoFront)))
        pub.publish(vel_msg)
        timee =timee+0.1 
       
        
        if (duration>timee):
            break
if __name__ == "__main__":
    rospy.init_node("hello")        

    
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=poseback)
    rate = rospy.Rate(2) 
    vel=float(input('enter car\'s velocity'))
    steerangl=float(input('enter the steering angle'))
    duration=float(input('enter the Duration of simulation'))
    
    CGtoFront= rospy.get_param("/CGtoFront")
    CGtoBack= rospy.get_param("/CGtoBack")

    move(duration,vel,steerangl)
    

   
  
