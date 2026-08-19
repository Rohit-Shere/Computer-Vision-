import cv2
import numpy as np 

canvas = np.zeros((512, 512,3), dtype = np.uint8)

cv2.line(canvas, (0,0), (511, 511), (100,200, 255), 10)

cv2.rectangle(canvas, (284,0), (510,128),(0,0,255),-1)

cv2.putText(canvas, "OpenCV text addition", org = (10,500),color=(0,200,255),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale=1)
cv2.imshow("Canvas with shapes", canvas)



cv2.waitKey(0)

cv2.destroyAllWindows()