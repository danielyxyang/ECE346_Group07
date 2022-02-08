#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from IPython import display
from threading import Lock
import matplotlib.pyplot as plt

# TODO: import the message type for the subscribed topic
# Use '''rostopic type ''' as shown in the readme to determine
# the proper type
from geometry_msgs.msg import PoseStamped

class PoseSubscriber:
    MAX_LIST_SIZE = 200

    '''
    This class subscribes to the ros "/zed2/zed_node/pose" topic, and 
    save the most recent 200 position [x,y] in to lists

    '''
    def __init__(self):
        self.x_traj = []
        self.y_traj = []
        # Lock to avoid thread race
        self.lock = Lock()
        '''
        TODO: Here you need to finish the rest of your subscriber class
        As we have done before, you may need to create some objects and 
        add some functions

        Hint 1: you need to use self.lock.acquire() before putting data to 
        the self.x_traj and self.y_traj lists
        After you finish adding value to lists, use self.lock.release()
        Checkout https://docs.python.org/3/library/threading.html#lock-objects 
        for more info

        Hint 2: You can do  self.x_traj.pop(0) to pop the first node in the list
        in order to maintain the maximum list size.
        '''
        rospy.init_node("pose_node", anonymous=True)

        self.sub_pose = rospy.Subscriber("/zed2/zed_node/pose", PoseStamped, self.callback)

    def callback(self, data):
        self.lock.acquire()

        if len(self.x_traj) != len(self.y_traj):
            self.x_traj.clear()
            self.y_traj.clear()
        
        while len(self.x_traj) > self.MAX_LIST_SIZE:
            self.x_traj.pop(0)
            self.y_traj.pop(0)
        
        self.x_traj.append(data.pose.position.x)
        self.y_traj.append(data.pose.position.y)

        self.lock.release()
 
if __name__ == "__main__":
    listener = PoseSubscriber()
    plt.ion()
    plt.show()
    plt.figure(figsize=(5, 5))

    while not rospy.is_shutdown():
        
        display.clear_output(wait = True)
        display.display(plt.gcf())
        plt.clf()

        # avoid thread race 
        listener.lock.acquire()
        plt.scatter(listener.x_traj, listener.y_traj)
        listener.lock.release()
        plt.xlim((-5, 5))
        plt.ylim((-5, 5))
        plt.pause(0.001)
        plt.pause(0.001)
