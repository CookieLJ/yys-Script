# coding=utf-8
import function


challengePic = function.importPic('yuling', 'challengePic')
endPic = function.importPic('yuling', 'victoryPic')
fudaiPic = function.importPic('yuling', 'fudaiPic')


def clickFunction(sp, res, box):
	clickRange = [sp[1], sp[0]]  # 点击范围
	x, y = function.getPoint(res, box[0], box[1], clickRange)
	function.moveCurPos(x, y)
	function.clickLeftCur()


def yuling(num):
	i = 0
	while 1:
		if i == num:
			break
		box = function.getWindowInfo()
		pic = function.screenShot(box)
		if function.match(pic, challengePic).max() > 0.75:
			i = i+1
			print 1
			res = function.match(pic, challengePic)
			sp = challengePic.shape
			clickFunction(sp, res, box)
			function.randomDelay(30, 30)		# 时间可以自己设置
		elif function.match(pic, endPic).max() > 0.75:
			print 2
			res = function.match(pic, challengePic)
			sp = challengePic.shape
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
		elif function.match(pic, fudaiPic).max() > 0.75:
			print 3
			res = function.match(pic, fudaiPic)
			sp = fudaiPic.shape
			clickFunction(sp, res, box)


if __name__ == '__main__':
	yuling(2)