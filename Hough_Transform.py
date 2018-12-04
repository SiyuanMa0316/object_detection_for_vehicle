import cv2

img=cv2.imread("Sample_Input.jpg")
cv2.namedWindow("Image")
cv2.imshow("img",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小
print(img.shape)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=5,maxRadius=300)
print(circles)
print(len(circles[0]))

for circle in circles[0]:
    print(circle[2])
    #X坐标
    x = int(circle[0])
    #Y坐标
    y = int(circle[1])
    #半径
    r = int(circle[2])
    img = cv2.circle(img,(x,y),r,(0,0,255),-1)

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()