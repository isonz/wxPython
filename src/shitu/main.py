#!/usr/bin/env python
# -*- coding: gbk -*- 

import PIL.Image

class Shitu:
    
    _image = None
    _txt = None
    
    def __init__(self, image, txt):
        self._image = image
        self._txt = txt
        self.getImageData()
        
    def getImageData(self, image=None, txt=None):
        if image is not None: self._image = image
        if txt is not None: self._txt = txt
        
        im = PIL.Image.open(self._image)
        img = im.convert('L')
        data  = img.getdata()
        self.saveImage(data, img, self._image)
            
    def saveDataToTxt(self, txt, data):
        try:
            f = open(txt, 'w')
            try:
                f.write(data)
            finally:
                f.close()
        except IOError, e:
            print e
        
    def saveImage(self, data, im, name):
        i=0
        tmp = 0
        dt = ''
        for y in range(im.size[0]):
            for x in range(im.size[1]):
                if (data[i]-tmp) < -30  or  (data[i]-tmp) > 30:
                    tmp = data[i]
                    
                if (255-tmp)<30: tmp = 255
                im.putpixel((x,y), tmp)
                i=i+1
                dt = dt + str(tmp) +"\n"
        im.save(name+'.jpg');
        self.saveDataToTxt(self._txt, dt)
        
    
if __name__ == "__main__":
    shitu = Shitu("../images/1.jpg", '1.txt')
    shitu = Shitu("../images/2.jpg", '2.txt')

    

