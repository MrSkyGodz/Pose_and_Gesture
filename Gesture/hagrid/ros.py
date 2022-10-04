import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import time
import model as M

# import rospy
# from sensor_msgs.msg import Image
device = "cpu"
class lanecv:
    def __init__(self):

        # rospy.init_node("Gesture")
        model = M._load_model("./SSDLite.pth", device)
        self.run = M.run(model, num_hands=100, threshold=0.8, landmarks= False)
        for i,j in enumerate(self.run):
                print(j)


        


def main():
    lane = lanecv()

if __name__ == "__main__" :
    main()