class FileOpr:
  def __init__(self, path):
    self.filepath_ = path
    try:
      self.fd_ = open(self.filepath_, "rb")
    except IOError:
      self.filerd_ = False
    else:
      self.filerd_ = True
      self.section_ = []
  def __del__(self):
    if self.filerd_:
      # print(self.fd_.fileno())
      self.fd_.close()
  def ReadSection(self, hintphrase):
    self.section_.clear()
    start = False
    while True:
      line = self.fd_.readline()
      if not line:
        if len(self.section_) > 0:
          return True
        else:
          return False
      if line.find(hintphrase.encode()) == 0 and not start:
        start = True
        self.section_.append(line)
        continue
      if start:
        #should be the next round, go back and break
        if line.find(hintphrase.encode()) == 0:
          self.fd_.seek(len(line) * -1, 1)
          return True
        else:
          self.section_.append(line)
  #extract what user want from section
  #if is user want, func return True, else return False
  def ExtractKeyLine(self, func, keyword):
    res = []
    for no in range(0, len(self.section_)):
      if func(self.section_[no], keyword):
        res.append(self.section_[no])
    return res


def lineheadedbykey(line, key):
  if line.find(key.encode()) == 0:
    return True
  return False

if __name__ == '__main__':
  fd = FileOpr("D:\\cmpshare\\github\\retinanet\\result\\505391_HighPrecision_raw_turbojpeg.txt")
  # newfd = FileOpr("D:\\haha.txt")
  if fd.ReadSection("file"):
    print(fd.ExtractKeyLine(lineheadedbykey, "vec"))
  if fd.ReadSection("file"):
    print(fd.ExtractKeyLine(lineheadedbykey, "vec"))
