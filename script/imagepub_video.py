#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import scipy
import cv2.cv as cv

rospy.init_node('VideoPublisher',anonymous=False)
VideoRaw = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
rate = rospy.Rate(50)



cam = cv2.VideoCapture(0)

while not rospy.is_shutdown():
    meta, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    msg_frame = CvBridge().cv2_to_imgmsg(frame, "mono8")
    msg_frame.header.stamp = rospy.Time.now()
    VideoRaw.publish(msg_frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    rate.sleep()
cam.release()
#----------------------------


cv2.destroyAllWindows()

