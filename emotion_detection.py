#importing libraries
!pip install deepface

import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

img = cv2.imread('/home/neosoft/Documents/emotion_imgs/download.jpeg')
plt.imshow(img[:,:,::-1])
plt.show()

result = DeepFace.analyze(img,actions=['emotion'])
#print(result)
result['dominant_emotion']
