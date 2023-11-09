# Test Classifier

import cv2 as cv
import mediapipe as mp
import pickle
import numpy as np

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)

labels_dict = {0: 'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 
			   14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

while True:

	data_aux = []
	x_ = []
	y_ = []

	ret, frame = cap.read()

	H, W, _ = frame.shape
	
	frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)	# Converts the image into RGB channels

	results = hands.process(frame_rgb)
	if results.multi_hand_landmarks:
		for hand_landmarks in results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(
				frame,
				hand_landmarks,
				mp_hands.HAND_CONNECTIONS,
				mp_drawing_styles.get_default_hand_landmarks_style(),
				mp_drawing_styles.get_default_hand_connections_style()
			)

		for hand_landmarks in results.multi_hand_landmarks:
			for i in range(len(hand_landmarks.landmark)):
				x = hand_landmarks.landmark[i].x
				y = hand_landmarks.landmark[i].y
				data_aux.append(x)
				data_aux.append(y)
				x_.append(x)
				y_.append(y)
		
		x1 = int(min(x_) * W) - 10
		y1 = int(min(y_) * H) - 10

		x2 = int(max(x_) * W) - 10
		y2 = int(max(y_) * H) - 10
		prediction = model.predict([np.asarray(data_aux)])

		predicted_char = labels_dict[int(prediction[0])]

		# print(predicted_char)
		cv.rectangle(frame, (x1, y1 - 10), (x2, y2), (0,0,0), 4)
		cv.putText(frame, predicted_char, (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1.3, (0,255,0), 3, cv.LINE_AA)

	cv.imshow('frame', frame)
	cv.waitKey(25)

cap.release()
cv.destroyAllWindows()