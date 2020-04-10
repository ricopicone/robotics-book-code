#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32 # standard int

# Setup: initialize node, register topic, set rate
rospy.init_node( # initialize node
  'topic_publisher' # node default name
)
pub = rospy.Publisher( # register topic w/roscore
  'counter', # topic name
  Int32, # topic type
  queue_size=5 # queue size
)
rate = rospy.Rate(2) # adaptive rate in Hz

# Loop: publish, count, sleep
count = 0
while not rospy.is_shutdown(): # until ctrl-c
    pub.publish(count) # publish count
    count += 1 # increment
    rate.sleep() # set by rospy.Rate above