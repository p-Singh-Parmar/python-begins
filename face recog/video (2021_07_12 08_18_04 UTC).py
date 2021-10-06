import cv2
import time

first_frame = None
video = cv2.VideoCapture(0)
a=1
while True:
    a = a + 1
    check, frame = video.read()
    print(frame)                    #time.sleep(3)  #stops the script for 3 seconds
    cv2.imshow('capturing', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()