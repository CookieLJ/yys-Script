#coding=utf8
import function


endPic = function.importPic('partner', 'victoryPic')
fudaiPic = function.importPic('partner', 'fudaiPic')


def clickFunction(sp, res, box):
    clickRange = [sp[1], sp[0]]  # 点击范围
    x, y = function.getPoint(res, box[0], box[1], clickRange)
    function.moveCurPos(x, y)
    function.clickLeftCur()


def partner(num):
    i = 0
    while 1:
        if i == num:
            break
        box = function.getWindowInfo()
        pic = function.screenShot(box)
        print function.match(pic, endPic).max()
        print function.match(pic, fudaiPic).max()
        if function.match(pic, endPic).max() > 0.8:
            print '胜利'
            res = function.match(pic, endPic)
            sp = endPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
        elif function.match(pic, fudaiPic).max() > 0.9:
            print 3
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.8)


if __name__ == '__main__':
    partner(10)