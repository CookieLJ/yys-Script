# coding=utf-8
import cv2
from PIL import ImageGrab

box = 100, 200, 300, 400
insScreenshot = ImageGrab.grab(box)  # 截图
insScreenshot.save('.\pic\insScr.png')  # 截图保存
position = 'yuling'
picName = 'victoryPic'
str = '.\pic\%s\%s.png' % (position, picName)
img = cv2.imread(str)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
print str
