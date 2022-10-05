import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import time
import model as M

import rospy
from std_msgs.msg import Int16
device = "cpu"

targets = {
    1: "call",
    2: "dislike",
    3: "fist",
    4: "four",
    5: "like",
    6: "mute",
    7: "ok",
    8: "one",
    9: "palm",
    10: "peace",
    11: "rock",
    12: "stop",
    13: "stop inverted",
    14: "three",
    15: "two up",
    16: "two up inverted",
    17: "three2",
    18: "peace inverted",
    19: "no gesture"
}


class Gesture:
    def __init__(self):

        rospy.init_node("Gesture")
        self.pub = rospy.Publisher('hand_ges', Int16, queue_size=0)

        model = M._load_model("./SSDLite.pth", device)
        self.run = M.run(model, num_hands=100, threshold=0.8, landmarks= False)
        for i,j in enumerate(self.run):
                print(j)
                self.pub.publish(Int16(j))


        


def main():
    Gesture()

if __name__ == "__main__" :
    main()