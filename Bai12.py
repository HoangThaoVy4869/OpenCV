# Bat vat the chuyen dong
from cv2 import cv2
import time
cap = cv2.VideoCapture("bida.mp4")   
##Chinh toc do video  
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000/fps
# Tach nhung thu khong chuyen dong theo nen
bg = cv2.createBackgroundSubtractorMOG2()
# Quy dinh so luong anh de loc nen
# Đặt giá trị số lượng của frame mà ảnh hưởng đến background
bg.setHistory(50)

while True:
    #Ham cap tra ve hai bien la ret va img
    ret,img = cap.read()
    pre_time = time.time()
    
    bgmask = bg.apply(img)

    bgmask = cv2.merge ([bgmask,bgmask,bgmask])

    result = cv2.bitwise_and(bgmask,img)

    cv2.imshow("Video",img)
    cv2.imshow("BgMask",bgmask)
    cv2.imshow("Result",result)
    delta_time = (time.time() - pre_time)*1000


    if delta_time > wait_time :
        delay_time = 1
    else:
        delay_time = wait_time - delta_time
    if cv2.waitKey(int(wait_time)) == ord ('q'):
        break

cv2.destroyAllWindows()