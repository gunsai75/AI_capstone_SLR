#  ------ WORK IN PROGRESS. I am just messing around with stuff ------

import cv2 as cv
import mediapipe as mp
import os
import matplotlib.pyplot as plt

DATA_DIR =  'learning/data'

for dir_ in os.listdir(DATA_DIR):
	for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
		img = cv.imread(os.path.join(DATA_DIR, dir_, img_path))
		img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

		plt.figure()
		plt.imshow(img_rgb)

plt.show()

#  ------ WORK IN PROGRESS. I am just messing around with stuff ------