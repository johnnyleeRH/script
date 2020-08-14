import cv2
import os

class CV:
  def __init__(self, inputdir, outputdir):
    self.inputdir_ = inputdir
    self.outputdir_ = outputdir
    if not os.path.exists(self.outputdir_):
      os.mkdir(self.outputdir_, 777)
    if self.inputdir_[-1] != '/':
      self.inputdir_ = self.inputdir_ + '/'
    if self.outputdir_[-1] != '/':
      self.outputdir_ = self.outputdir_ + '/'

  def Rectangle(self, imgin, pointvec, prename = ""):
    img = cv2.imread(self.inputdir_ + imgin, cv2.IMREAD_COLOR)
    color = (255, 255, 255)
    for index in range(len(pointvec)):
      cv2.rectangle(img, (int(float(pointvec[index][0])), int(float(pointvec[index][1]))), 
        (int(float(pointvec[index][2])), int(float(pointvec[index][3]))),
        color=color, thickness=2)
    cv2.imwrite(self.outputdir_ + prename + imgin, img)
  def SetScale(self, originwidth, originheight, scaledwidth, scaledheight):
    self.widthscale = float(originwidth / scaledwidth)
    self.heightscale = float(originheight / scaledheight)
  def OpenFile(self, imgin):
    self.img_ = cv2.imread(self.inputdir_ + imgin, cv2.IMREAD_COLOR)
  def Rectangle(self, pointvec, color):
    for index in range(len(pointvec)):
      cv2.rectangle(self.img_, (int(pointvec[index][0]*self.widthscale), int(pointvec[index][1]*self.heightscale)), 
        (int(pointvec[index][2]*self.widthscale), int(pointvec[index][3]*self.heightscale)),
        color=color, thickness=2)
  def WriteFile(self, imgout):
    cv2.imwrite(self.outputdir_ + imgout, self.img_)