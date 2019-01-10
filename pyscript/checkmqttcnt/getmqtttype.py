CANDIDATE = "/home/lrhcmp/cmpshare/pyscript/checkmqttcnt/candidate.txt"
ORIGIN = "/home/lrhcmp/cmpshare/pyscript/checkmqttcnt/newmqtt"
 
if __name__=='__main__':
  candi = open(CANDIDATE, 'r')
  candifile = []
  while True:
    line = candi.readline()
    if not line:
      break
    if line.strip() not in candifile:
      candifile.append(line.strip())
  candi.close()
  origin = open(ORIGIN, 'r')
  matchfile = []
  event = []
  while True:
    line = origin.readline()
    if not line:
      break
    # line = line.strip()
    for target in candifile:
      if -1 != line.find(target):
        if -1 != line.find('6333c61d-371e-4f57-a969-6d218ecec9b4'):
          event.append(line)
        if -1 != line.find('\"ptype\":8'):
          matchfile.append(line)
          break
  origin.close()
  print "[%d:%d]" % (len(matchfile), len(candifile))
  print "%d" % len(event)
  # print candifile