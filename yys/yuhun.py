# coding=utf-8
'''win32控制台'''
import win32gui
import win32con
import win32api
import win32con

'''移动鼠标需要'''
from ctypes import *

'''图片处理cv'''
import cv2

'''随机数'''
import random

'''截图'''
from PIL import ImageGrab

'''时间库'''
import time



def clickLeftCur():
	# 点击鼠标 需要管理员权限
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def moveCurPos(x, y):  # 移动鼠标
	windll.user32.SetCursorPos(x, y)


def getWindowInfo():
	# 获得句柄
	wdname = u'阴阳师-网易游戏'
	handle = win32gui.FindWindow(0, wdname)  # 获得句柄
	x1, y1, x2, y2 = win32gui.GetWindowRect(handle)  # 获得窗口坐标
	box = x1, y1, x2, y2
	# print (x1, y1, x2, y2)
	return box


def screenShot(box):
	# 截图
	# box为窗口坐标
	randomDelay(0.5,1)
	insScreenshot = ImageGrab.grab(box)  # 截图
	insScreenshot.save('d:\yys\insScr.png')  # 截图保存
	img = cv2.imread('d:\yys\insScr.png', 0)  # 打开图片
	return img


def match(img1, img2):
	# 图像匹配
	# img1为即时截图，
	# img2为匹配图
	res = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
	return res


def randomDelay(a, b):
	# 随机延迟
	time.sleep(random.uniform(a, b))


def randomLocation(x, y):
	# 随机位置
	# x,y均为数组
	xl = random.randint(x[0], x[1])
	yl = random.randint(y[0], y[1])
	return xl, yl


def getPoint(res, upperLeftCornerXCoordinate, upperLeftCornerYCoordinate, clickRange):
	# 点击坐标
	# res为图像匹配返回二维图像
	# upperLeftCornerXCoordinate为窗口左上角的x坐标
	# upperLeftCornerXCoordinate为窗口左上角的y坐标
	# clickRange为匹配图像的像素
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	xRange = [upperLeftCornerXCoordinate + max_loc[0], upperLeftCornerXCoordinate + max_loc[0] + clickRange[0]]
	yRange = [upperLeftCornerYCoordinate + max_loc[1], upperLeftCornerYCoordinate + max_loc[1] + clickRange[1]]
	x, y = randomLocation(xRange, yRange)
	return x, y


def begin():
	startImg = cv2.imread('d:\yys\start.png', 0)
	endImg = cv2.imread('d:\yys\end.png', 0)
	fudaiImg = cv2.imread('d:\yys\click.png', 0)
	teamImg = cv2.imread('d:\yys\individual.png', 0)
	n = input("Number limit:")
	n = int(n)
	return startImg, endImg, fudaiImg, teamImg, n


def display(n):
	if n % 10 == 1:
		print n, 'st time'
	elif n % 10 == 2:
		print n, 'nd time'
	elif n % 10 == 3:
		print n, 'rd time'
	else:
		print n, 'th time'


def matchTouch(startImg,teamImg):
	# 点击函数
	# startImg为 ‘开始 ’匹配模板
	box = getWindowInfo()
	insInterface = screenShot(box)
	res = match(insInterface, teamImg)
	'''首先判断是否在组队'''
	n = 1
	while 1:
		print 'start match:'
		display(n)
		if res.max() > 0.97:
			break
		else:
			insInterface = screenShot(box)
			res = match(insInterface, teamImg)
			n += 1
	insInterface = screenShot(box)
	res = match(insInterface, startImg)
	'''点击范围'''
	sp = startImg.shape
	clickRange = [sp[1], sp[0]-5]
	print '(', sp[1], ',', sp[0], ')'
	x, y = getPoint(res, box[0], box[1], clickRange)
	print 'click coordinate:', '(', x, ',', y, ')'
	moveCurPos(x, y)
	clickLeftCur()


def endClick(endImg, fudaiImg):
	box = getWindowInfo()
	insInterface = screenShot(box)
	res = match(insInterface, endImg)
	n = 1
	print 'end match'
	while 1:
		display(n)
		print res.max()
		if res.max() > 0.5:
			break
		else:
			n += 1
			insInterface = screenShot(box)
			res = match(insInterface, endImg)
	insInterface = screenShot(box)
	res = match(insInterface, endImg)
	'''点击范围'''
	sp = fudaiImg.shape
	clickRange = [sp[1], sp[0]]
	print '(', sp[1], ',', sp[0], ')'
	for i in range(1, 4):
		print 'end click', display(i)
		x, y = getPoint(res, box[0], box[1], clickRange)
		print 'click coordinate:', '(', x, ',', y, ')'
		randomDelay(0.5, 1.5)
		moveCurPos(x, y)
		clickLeftCur()
	randomDelay(1, 2)
	insInterface = screenShot(box)
	res = match(insInterface, fudaiImg)
	if res.max() > 0.5:
		print 'click the fudai'
		sp = fudaiImg.shape
		print '(', sp[1], ',', sp[0], ')'
		clickRange = [sp[1], sp[0]]
		x, y = getPoint(res, box[0], box[1], clickRange)
		print 'click coordinate:', '(', x, ',', y, ')'
		moveCurPos(x, y)
		clickLeftCur()

if __name__ == '__main__':
	startImg, endImg, fudaiImg, teamImg, n = begin()
	for k in range(1, n+1):
		print 'start to yuhun'
		display(k)
		matchTouch(startImg, teamImg)
		print ('fighting...wait...')
		randomDelay(20, 20)  # 可写成键入等待
		endClick(endImg, fudaiImg)
		randomDelay(0.5, 1.5)


# 测试代码

