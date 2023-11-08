import cv2 as cv
import mediapipe as mp
import os
import pickle

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)	# Mediapipe recognition system amongus

DATA_DIR =  'learning/data' # Directory where the data is stored

data = []	# Array of data points
labels = []	# Array of labels

for dir_ in os.listdir(DATA_DIR):
	for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
		data_aux = []	# A list containing arrays
		img = cv.imread(os.path.join(DATA_DIR, dir_, img_path))		# Reads each image in the directory
		img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)	# Converts the image into RGB channels

		results = hands.process(img_rgb)
		if results.multi_hand_landmarks:
			for hand_landmarks in results.multi_hand_landmarks:
				for i in range(len(hand_landmarks.landmark)):
					x = hand_landmarks.landmark[i].x
					y = hand_landmarks.landmark[i].y
					data_aux.append(x)
					data_aux.append(y)
				
			data.append(data_aux)	# Appends array into data object
			labels.append(dir_)		# Appends the directory names into labels object

f = open('data.pickle', 'wb')	# Creates data.pickle in the working directory
pickle.dump({'data': data, 'labels': labels}, f)	# Writes the data and labels into the file
f.close()