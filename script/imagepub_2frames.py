#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import scipy

rospy.init_node('VideoPublisher',anonymous=False)
VideoRaw = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
rate = rospy.Rate(50)


# """
#publish images from a camera
#----------------------------
img1 = cv2.imread('/home/abhishek/my_catkin_ws/src/correlation_flow/script/1.jpg')
img2 = cv2.imread('/home/abhishek/my_catkin_ws/src/correlation_flow/script/2.jpg')

i=0;
while not rospy.is_shutdown():
    
    msg_frame = CvBridge().cv2_to_imgmsg(img1, "bgr8")
    t = rospy.Time.now()
    msg_frame.header.stamp=rospy.Duration(0.03)
    
    VideoRaw.publish(msg_frame)
    rospy.sleep(0.1)
    cv2.imshow('frame', img1)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


    i=1;
    msg_frame2 = CvBridge().cv2_to_imgmsg(img2, "bgr8")
    msg_frame2.header.stamp=rospy.Duration(0.03)
    VideoRaw.publish(msg_frame2)
    cv2.imshow('frame', img2)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    rate.sleep()
#----------------------------
cv2.destroyAllWindows()

