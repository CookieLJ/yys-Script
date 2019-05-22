# coding=utf-8
import function

challengePic = function.importPic('challengePic')  # challengePic 开始挑战图片
endPic = function.importPic('endPic')  # endPic 结束挑战图片
fudaiPic = function.importPic('fudaiPic')


def chi(num):
    # num 次数
    i = 0
    while 1:
        if i == num:
            break
        box = function.getWindowInfo()
        pic = function.screenShot(box)  # type: box
        if function.match(pic, challengePic).max() > 0.75:
            print 1
            res = function.match(pic, challengePic)
            print res.max()
            i = i+1
            sp = challengePic.shape
            clickRange = [sp[1], sp[0]]  # 点击范围
            x, y = function.getPoint(res, box[0], box[1], clickRange)
            function.moveCurPos(x, y)
            function.clickLeftCur()
            function.randomDelay(50, 50)
        elif function.match(pic, endPic).max() > 0.75:
            print 2
            res = function.match(pic, endPic)
            print res.max()
            sp = endPic.shape
            clickRange = [sp[1], sp[0]]
            x, y = function.getPoint(res, box[0], box[1], clickRange)
            function.moveCurPos(x, y)
            function.clickLeftCur()
            function.randomDelay(0.3, 0.8)
            x, y = function.getPoint(res, box[0], box[1], clickRange)
            function.moveCurPos(x, y)
            function.clickLeftCur()
            function.randomDelay(0.3, 0.8)
            x, y = function.getPoint(res, box[0], box[1], clickRange)
            function.moveCurPos(x, y)
            function.clickLeftCur()
        elif function.match(pic, fudaiPic).max() > 0.75:
            print 3
            res = function.match(pic, fudaiPic)
            print res.max()
            sp = fudaiPic.shape
            clickRange = [sp[1], sp[0]]
            x, y = function.getPoint(res, box[0], box[1], clickRange)
            function.moveCurPos(x, y)
            function.clickLeftCur()


if __name__ == '__main__':
    chi(20)


