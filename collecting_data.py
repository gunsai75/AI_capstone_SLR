# Importing necessary modules
import os
import cv2 as cv

# Creating working directory
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
	os.makedirs(DATA_DIR)

number_of_classes = 26  # 26 classes for 26 alphabets
dataset_size = 100  # kept 100 for primitive testing

# Using the camera peripheral to capture data
cap = cv.VideoCapture(0)	# Argument set to '0' to capture from first connected camera
for j in range(number_of_classes):
	if not os.path.exists(os.path.join(DATA_DIR, str(j))):
		os.makedirs(os.path.join(DATA_DIR, str(j)))		# Making a directory for each class
	
	print('Collecting data for class {}'. format(j))

	done = False
	while True:
		ret, frame = cap.read()
		cv.putText(frame, 'Ready? Press "Q" ', (100,50), cv.FONT_HERSHEY_SIMPLEX, 1.3, (0,255,0), 3, cv.LINE_AA)
		cv.imshow('frame', frame)
		if cv.waitKey(25) == ord('q'):
			break

	counter=0
	while counter < dataset_size:
		ret, frame = cap.read()
		cv.imshow('frame', frame)	# Shows what the camera is capturing at real-time 
		cv.waitKey(25)
		cv.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)	# Naming each image

		counter += 1

cap.release()
cv.destroyAllWindows()