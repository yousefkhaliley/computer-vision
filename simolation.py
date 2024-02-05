
import cv2
import mediapipe as mp
import numpy as np
from matplotlib import pyplot as plt

# initialize mediapipe pose solution
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()



# take live camera  input for pose detection
cap = cv2.VideoCapture(0)

# read each frame/image from capture object
while True:
    ret, img = cap.read()
    if ret==False:
        break
    # resize image/frame so we can accommodate it on our screen
    img = cv2.resize(img, (800, 600))

    # do Pose detection
    results = pose.process(img)
    # draw the detected pose on original video/ live stream
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2)
                           )
    # Display pose on original video/live stream
    cv2.imshow("Pose Estimation", img)

    # Extract and draw pose on plain white image
    h, w, c = img.shape   # get shape of original frame
    opImg = np.zeros([h, w, c])  # create blank image with original frame size
    opImg.fill(0)  # set white background. put 0 if you want to make it black

    # draw extracted pose on black white image
    mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2)
                           )
    # display extracted pose on blank images
    cv2.imshow("Extracted Pose", opImg)

    # print all landmarks
    print(results.pose_landmarks)

    
    if cv2.waitKey(1)== ord('q'):
        break
        


cv2.destroyAllWindows()
cap.release()