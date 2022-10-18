import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, 
"Sun", 
(20,250), 
cv2.FONT_HERSHEY_COMPLEX, 
1,
(255,255,255))

cv2.putText(img, 
"Mercury", 
(110,250), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Venus", 
(200,250), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Earth", 
(290,250), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Mars", 
(380,250), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Jupiter", 
(550,350), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Saturn", 
(750,300), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Uranus", 
(970,275), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"Neptune", 
(1099,275), 
cv2.FONT_HERSHEY_COMPLEX, 
0.5,
(255,255,255))

cv2.putText(img, 
"THE SOLAR SYSTEM", 
(500,50), 
cv2.FONT_HERSHEY_COMPLEX, 
1,
(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)