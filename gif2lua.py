import cv2
from PIL import Image
import numpy
import math

crgb = [[240, 240, 240],[242, 178, 51],[229, 127, 216],[153, 178, 242],[222, 222, 108],[127, 204, 25],[242, 178, 204],[76, 76, 76],[153, 153, 153],[76, 153, 178],[178, 102, 229],[51, 102, 204],[127, 102, 76],[87, 166, 78],[204, 76, 76],[17, 17, 17]]
cname = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]

h = 52
w = 100

def getClosestColor(rgb):
    lowestDiff = 765
    retClr = None
    cnt = 0
    for clr in crgb:
        #cdiff = math.sqrt(((rgb[0]-clr[0])*0.3)**2 + ((rgb[1]-clr[1])*0.59)**2 + ((rgb[2]-clr[2])*0.11)**2)
        cdiff = math.sqrt(((rgb[0]-clr[0]))**2 + ((rgb[1]-clr[1]))**2 + ((rgb[2]-clr[2]))**2)
        if cdiff < lowestDiff:
            lowestDiff = cdiff
            retClr = cname[cnt]
        cnt += 1
    return retClr

gimg = Image.open("endgoal.gif")

f = open('luacode.txt','w',encoding=None)
f.write('function s(m,clr,numspace)\n')
f.write('    m.setBackgroundColor(clr);')
f.write('m.write(string.rep(\' \',numspace))\n')
f.write('BACKSPACE!\n')
f.write('end;')
f.write('m = peripheral.find(\'monitor\');')
f.write('m.setTextScale(0.5)\n')
f.write('while 1 do\n    ')
curSize = 0
for a in range(gimg.n_frames):
    gimg.seek(a)
    img = numpy.array(gimg.resize((w,h), Image.Resampling.LANCZOS).convert('RGB'))
    for i in range(h):
        sLine = 'm.setCursorPos(1,' + str(i+1) + ');'
        if (curSize + len(sLine) > 480):
            f.write("\n")
            curSize = 0
        curSize += len(sLine)
        f.write(sLine)
        sneedFlag = False
        prevColor = None
        numSpaces = 1
        for j in range(w):
            bgr = img[i,j]
            rgb = [bgr[0],bgr[1],bgr[2]]
            curColor = getClosestColor(rgb)
            if sneedFlag == False:
                prevColor = curColor
                sneedFlag = True
            if curColor == prevColor:
                numSpaces += 1
            else:
                line = 's(m,' + str(prevColor) + ',' + str(numSpaces) + ');'
                if (curSize + len(line) > 480):
                    f.write("\n")
                    curSize = 0
                f.write(line)
                curSize += len(line)
                numSpaces = 1
            prevColor = curColor
        if numSpaces != 0:
            line = 's(m,' + str(prevColor) + ',' + str(numSpaces) + ');'
            if (curSize + len(line) > 480):
                    f.write("\n")
                    curSize = 0
            curSize += len(line)
            f.write(line)
    sleepFor = gimg.info["duration"]
    print(sleepFor/1000)
    f.write('os.sleep(' + str(sleepFor/1000) + ');')
f.write('\nBACKSPACE!\n')
f.write('end;')