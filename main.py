import numpy as np
import cv2
from PIL import Image
import urllib.request as request
import time
url = "http://192.168.0.105:4747/cam/1/frame.jpg"
#cap = cv2.VideoCapture(0)
alpha = 2 # Contrast control
beta = 5 # Brightness control
filename = "scanned document"
extension = '.pdf'
while True:
    img = request.urlopen(url)
    img_arr = bytearray(img.read())
    imgnp = np.array(img_arr,dtype=np.uint8)
    frame = cv2.imdecode(imgnp,-1)
    frame = cv2.imdecode(imgnp, -1)
    #ret, frame = cap.read()
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    og = frame
    frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
    # Code Here
    frame = cv2.Canny(frame,300,500)
    cntrs , h = cv2.findContours(frame,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    if cntrs:
        maxc = max(cntrs,key=cv2.contourArea)
        x , y , w , h = cv2.boundingRect(maxc)
        cv2.rectangle(og,(x,y),(x+w,y+h),(0,255,255),2)
    if (cv2.waitKey(1) == ord('s')):
        moment = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil = Image.fromarray(frame)
        img_pil.save(filename + moment + extension)
        print(f"Saved as \"{filename + moment + extension}\"")



    cv2.imshow('processed', og)
    #cv2.imshow('original', og)
    # press escape to exit
    if (cv2.waitKey(1) == 27):
        break
cap.release()
cv2.destroyAllWindows()
