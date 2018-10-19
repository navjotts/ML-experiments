import os
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(frame):
    cv2.imshow('image', frame)
    cv2.waitKey(0)
    print(frame.shape)
    # each frame is an image, which an be played around with ML models

if __name__ == '__main__':
    cap = cv2.VideoCapture(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos', 'test.mp4'))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break