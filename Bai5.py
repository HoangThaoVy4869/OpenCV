# Phat video theo toc do
from cv2 import cv2
import time
cap = cv2.VideoCapture("bida.mp4")   
##Chinh toc do video  
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000/fps
print(fps)
while True:
    #Ham cap tra ve hai bien la ret va img
    ret,img = cap.read()
    pre_time = time.time()
    img = cv2.medianBlur(img,3)
    cv2.imshow("Video",img)
    delta_time = (time.time() - pre_time)*1000
    print (delta_time)

    if delta_time > wait_time :
        delay_time = 1
    else:
        delay_time = wait_time - delta_time
    if cv2.waitKey(int(wait_time)) == ord ('q'):
        break

cv2.destroyAllWindows()
