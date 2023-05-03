# import the opencv library
import cv2
import time
  
# define a video capture object
vid = cv2.VideoCapture(0)
prev = 0
frame_rate = 10
starting_time = time.time()

while time.time() - starting_time <= 1:
    time_elapsed = time.time() - prev
    if time_elapsed > 1./frame_rate:
        print("FPS:", 1/time_elapsed)
        prev = time.time()
        ret, frame = vid.read()
        # cv2.imshow('frame', frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()