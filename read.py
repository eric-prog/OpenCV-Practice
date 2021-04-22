import cv2 as cv

# IMAGES
# img = cv.imread("Photos/cat.jpeg")

# cv.imshow("Cat", img)

# VIDEOS
capture = cv.VideoCapture("Videos/video1.mp4")

while True:
    isTrue, frame = capture.read() # reads video frame by frame. IsTrue is whether frame was read properly
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"): # break out of while loop. If d is pressed stop.
        break; 


# cv.waitKey(0) 
capture.release() # release capture device
cv.destroyAllWindows() 
