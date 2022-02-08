#!/usr/bin/env python
import rospy
# TODO: Import the correct message type for subscribing and publishing
# checkout the section 2.5.2 in lab0.pdf for example
from geometry_msgs.msg import Twist
from rc_control_msgs.msg import RCControl

class ControlNode:
    '''
    This class subscribe to "/cmd_vel" topics with type geometry_msgs/Twist
    from the keyboard control node.
    Then it translates the keyboard's message into a rc_control_msgs/RCControl message,
    and publish it with topic "/rc_control"
    '''
    def __init__(self):

        rospy.init_node("keyboard_listener", anonymous=True)

        '''
        TODO: Define your pubshiler and subscriber here
        '''
        self.sub_cmd_vel = rospy.Subscriber("cmd_vel", Twist, self.callback)
        self.pub_rc_control = rospy.Publisher("rc_control", RCControl, queue_size=10)

        rospy.spin()
        
    def callback(self, data):
        '''
        TODO: This is the callback function of you subscriber to the 
        keyboard control topic. 
        1. You will need to extract the 
            - linear.x as our throttle input
            - angular.z as our steering input
           from the subscribed message
        2. You need to construct a RCControl message and publish it
        '''
        throttle = data.linear.x
        steer = data.angular.z

        # rospy.loginfo("Throttle: {}".format(throttle))
        # rospy.loginfo("Steer:    {}".format(steer))

        msg_rccontrol = RCControl(throttle=throttle, steer=steer)
        self.pub_rc_control.publish(msg_rccontrol)
        

if __name__ == "__main__":
    talker = ControlNode()

