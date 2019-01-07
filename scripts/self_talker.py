#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time

pub_time_ros = None
pub_time = None

def callback(msg):
    delta_time = pub_time - time.time()
    delta_time_ros = pub_time_ros - rospy.get_time()    
    rospy.loginfo("I heard: %s", msg.data)
    rospy.logwarn("delta time ROS: %.5f, delta time: %.5f, delta-delta time: %.3f (microsec)", delta_time_ros, delta_time, (delta_time_ros - delta_time) * 1000000)

def shutdown():
    global sub
    sub.unregister()    
    rospy.loginfo("Goodbye!")

def talker():
    global sub, pub_time, pub_time_ros

    rospy.init_node('talker', anonymous=True)

    rospy.on_shutdown(shutdown)

    sub = rospy.Subscriber("chatter", String, callback)    

    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.get_param('~rate', 1)
    ros_rate = rospy.Rate(rate)

    rospy.loginfo("Starting ROS node talker...")

    while not rospy.is_shutdown():
        msg = "Greetings humans!"

        pub_time = time.time()
        pub_time_ros = rospy.get_time()
        pub.publish(msg)
        ros_rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        shutdown()
        
