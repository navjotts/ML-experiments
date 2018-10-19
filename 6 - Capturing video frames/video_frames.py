import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(frame):
    print(frame.shape)
    cv2.imshow('image', frame)
    cv2.waitKey(0)

if __name__ == '__main__':
    cap = cv2.VideoCapture('videos/test.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break