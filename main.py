import mediapipe as mp
import numpy as np
import cv2
mp_pose = mp.solutions.pose
draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()
fourc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourc,15.0,(680,400))
out_1 = cv2.VideoWriter('output_1.avi',fourc,15.0,(680,400))
cap = cv2.VideoCapture('D:\\yolo\\Custom_object_detection mask\\testing files\\video.mp4')
while(cap.read()):
    res, frame = cap.read()
    frame = cv2.resize(frame,(680,400))
    result = pose.process(frame)
    #print(result.pose_landmarks)
    h,w,c = frame.shape
    draw.draw_landmarks(frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS,draw.DrawingSpec((132,150,0),2,2),draw.DrawingSpec((255,0,0),1,1))
    img = np.zeros([h,w,c],np.uint8)
    img.fill(255)
    draw.draw_landmarks(img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS,draw.DrawingSpec((0,255,0),2,2),draw.DrawingSpec((255,0,0),2,2))
    cv2.imshow('white',img)
    cv2.imshow('img', frame)
    out.write(frame)
    out_1.write(img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    #cv2.imshow('img',frame)

cv2.destroyAllWindows()
