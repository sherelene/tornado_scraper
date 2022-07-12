import cv2
vidcap = cv2.VideoCapture('alexanderhall-1424874106353242116-20210809_162354-vid1.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
  cv2.imwrite("video_images/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1