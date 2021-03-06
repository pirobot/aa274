#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard: %s", msg.data)

def self_talker():
    rospy.init_node('talker', anonymous=True)

    sub = rospy.Subscriber("chatter", String, callback)    

    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.get_param('~rate', 1)
    ros_rate = rospy.Rate(rate)

    rospy.loginfo("Starting ROS node talker...")

    while not rospy.is_shutdown():
        msg = "Greetings humans!"
        
        pub.publish(msg)

        rospy.logwarn("Publishing %s", msg)
        
        ros_rate.sleep()

if __name__ == '__main__':
    try:
        self_talker()
    except rospy.ROSInterruptException:
        pass
        
