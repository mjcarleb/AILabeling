import cv2

video = cv2.VideoCapture("data/Cactus 4_8_22_V3.mp4")

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver) < 3:
    fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
else:
    fps= video.get(cv2.CAP_PROP_FPS)

spf = 1/fps
mspf = spf * 1000
a=3


ret, frame = video.read()
while(1):
   ret, frame = video.read()
   #cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
       video.release()
       cv2.destroyAllWindows()
       break
   cv2.imshow('frame',frame)
   a=3