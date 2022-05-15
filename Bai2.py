from cv2 import cv2
import numpy as np
# Tao ra mang co kich thuoc 600x800 voi do sau(mau) la do, xanhla, xanh duong
img = np.empty((600,800,3))
# Voi so 0 la mau do, so 1 mau xanhla, so 2 la mauduong
img[0:600,0:800,]=225

# ve line voi toa do diem dau la (300,400) toa do diem cuoi la 
# (10,10), mau den, voi do day cua line la 3
# cv2.line(img,(300,400),(10,10),(0,0,0,3)
# Vong lap range 
# ve duong ngang
for i in range (0,600,50):
    cv2.line(img,(0,i),(10,i),(0,0,0),2)
    #danh so theo duong
    cv2.putText(img,str(i),(10,i),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
# ve duong doc
for i in range (0,600,50):
    cv2.line(img,(i,0),(i,10),(0,0,0),2)
    cv2.putText(img,str(i),(i,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
#ve duong tron
cv2.circle(img,(90,96),50,(0,0,225))
# ve ellipse
cv2.ellipse(img,(300,300),(100,50),45,0,180,(0,4,878))
# ve dagiac
# ham pts cho biet toa do cac dinh trong da giac va kieu bien phai 
# la integer32 bit 
pts = np.array(((0,0),(50,50),(300,100),(100,100)),np.int32)
# Tham so hinh 3 chieu
pts = [pts.reshape((4,1,2))]
# voi thong so lan luot la tap hop dinh,hinh co kin hay k, mau sac
cv2.polylines(img,pts,True,(0,255,0))

cv2.imshow("Anh",img)
cv2.waitKey()