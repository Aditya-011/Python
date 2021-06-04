import cv2
import winsound
# intialize the video capture
cam = cv2.VideoCapture(0)
# run a loop to get frames
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    # get difference between two frames
    dif = cv2.absdiff(frame1,frame2)
    # convert rgb result to grayscale
    gray = cv2.cvtColor(dif, cv2.COLOR_RGB2GRAY)
    # generate the blur in the frame difference
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thres = cv2.threshold(blur, 20 , 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thres, None, iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1, (0,255,0),2)
    # make rectangle for big movements contours
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.PlaySound("alert.wav",winsound.SND_ASYNC)
    # exit from program on "q" keypress
    if cv2.waitKey(10) == ord('q'):
        break
    # show the output frames
    cv2.imshow('Camera', frame1)
