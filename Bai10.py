# Chon vat the_Xu ly chuot
from cv2 import cv2
import time

# Su kien xay ra khi nhap chuot
def Mouse_event(event, x, y, f, img):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Toa do luc nhan chuot xuong thi ve
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.draw = True

    if event == cv2.EVENT_LBUTTONUP:
        # Toa do luc tha chuot ra thi k ve nua
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        # Luu hinh anh da lay thanh mot anh moi
        miny = min(Mouse_event.y0,Mouse_event.y1)
        maxy = max(Mouse_event.y0, Mouse_event.y1)

        minx = min(Mouse_event.x0, Mouse_event.x1)
        maxx = max(Mouse_event.x0, Mouse_event.x1)

        # Keo chuot de chon anh theo toa do x,y
        Mouse_event.img = img[miny:maxy,minx:maxx]

    if event == cv2.EVENT_MOUSEMOVE:
        # Toa do khi re chuot thi k ve
        Mouse_event.x = x
        Mouse_event.y = y

Mouse_event.img = None
# Toa do luc nhan chuot xuong
Mouse_event.x0 = 0
Mouse_event.y0 = 0
# Toa do luc tha chuot ra
Mouse_event.x1 = 0
Mouse_event.y1 = 0
# Toa do khi re chuot
Mouse_event.x = 0
Mouse_event.y = 0
# Toa do sau khi ve
Mouse_event.draw = False


cap = cv2.VideoCapture("tracking.mp4") 
# Chinh toc do video  
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 10000/fps
print(fps)

while True:
    pre_time = time.time()
    ret,img = cap.read()
    img_clone = img.copy() # In ra ban copy cua anh

    if Mouse_event.draw:
        img_clone = cv2.rectangle(img_clone,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is not None: # Neu trong vung quet da chua anh thi in ra ban copy
        cv2.imshow("Sample", Mouse_event.img)

    cv2.imshow("Video", img_clone)
    cv2.setMouseCallback("Video",Mouse_event,img)


    if cv2.waitKey(int(wait_time)) == ord('q'):
        break
cv2.destroyAllWindows()