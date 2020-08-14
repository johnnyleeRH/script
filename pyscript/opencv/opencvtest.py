from opencv import *

if __name__ == "__main__":
    peoplevec = []
    people = [189, 3, 197, 25]
    peoplevec.append(people)
    people = [277, 95, 289, 142]
    peoplevec.append(people)
    feijivec = []
    feiji = [123, 91, 137, 126]
    feijivec.append(feiji)
    jivec = []
    ji = [195, 9, 232, 74]
    jivec.append(ji)
    ji = [157, 18, 187, 69]
    jivec.append(ji)
    ji = [235, 271, 314, 388]
    jivec.append(ji)
    cvtest = CV("/home/lrh/cmpshare/hisinnie/svp/build", "/home/lrh/cmpshare/hisinnie/svp/build")
    cvtest.SetScale(1633, 814, 416, 416)
    cvtest.OpenFile("jifeirentest.jpg")
    cvtest.Rectangle(peoplevec, (255, 0, 0))
    cvtest.Rectangle(feijivec, (0, 255, 0))
    cvtest.Rectangle(jivec, (0, 0, 255))
    cvtest.WriteFile("result.jpg")