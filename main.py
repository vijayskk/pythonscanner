import numpy as np
import cv2
from PIL import Image
import time

cap = cv2.VideoCapture(0)

filename = "scanned document"
extension = '.pdf'
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
    # Code Here

    if (cv2.waitKey(1) == ord('s')):
        moment = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil = Image.fromarray(frame)
        img_pil.save(filename + moment + extension)
        print(f"Saved as \"{filename + moment + extension}\"")



    cv2.imshow('webcam', frame)
    # press escape to exit
    if (cv2.waitKey(30) == 27):
        break
cap.release()
cv2.destroyAllWindows()
