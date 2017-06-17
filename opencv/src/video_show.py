
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# read from a video file
#cap = cv2.VideoCapture('vtest.avi')

# save a video file
# fourcc: codec (http://www.fourcc.org/codecs.php)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('out.avi', fourcc, 20, (640, 480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)

    # save frame
    #out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
#out.release()
cv2.destroyAllWindows()