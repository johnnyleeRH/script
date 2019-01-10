import telnetlib
import time

commands = ['wtdgops stop', 'ps axu | grep ovfs_smart']

totalcnt = 0


def check_smart_exist(oprresult):
  if -1 != oprresult.find('/root/runtime/face/bin/ovfs_smart'):
    return True
  return False

def conn_to_ipc(host, username, password):
  tn = telnetlib.Telnet(host, port=23, timeout=5)
  tn.read_until('login: ')
  tn.write(username + '\n')
  tn.read_until('Password: ')
  tn.write(password + '\n')
  #wait for prompt
  tn.read_until('~ #')
  return tn


def do_telnet(host, username, password):
  try:
    global totalcnt
    #exec command
    tn = conn_to_ipc(host, username, password)
    for command in commands:
      tn.write('%s\n' % command)
      time.sleep(20)
    tn.write("exit\n")
    #smart exist
    if check_smart_exist(tn.read_all()):
      tn.close()
      tn = conn_to_ipc(host, username, password)
      tn.write('reboot\n')
      tn.write("exit\n")
      tn.read_all()
      totalcnt = totalcnt + 1
      print "reboot cnt %d" % totalcnt
      return True
    else:
      tn.close()
      print "last reboot cnt %d" % totalcnt
      return False
  except:
    return True
 
if __name__=='__main__':
  host = '10.64.31.9'
  username = 'root'
  password = 'antslq'
  while True:
    if not do_telnet(host, username, password):
      break
    time.sleep(1)