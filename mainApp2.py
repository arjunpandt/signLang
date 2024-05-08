import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model
import numpy as np
import time
import pandas as pd
import pyttsx3
import threading

# model = load_model('/home/nashtech/PycharmProjects/kodeKombatML/src/model/saved_models/smnist_20epochs.h5')
model = load_model('/home/nashtech/PycharmProjects/kodeKombatML/src/notebooks/model_resnet.h5')


# functions to play the audio
def voice_message(eng, message):
    eng.say(message)
    eng.runAndWait()


# Setting parameters for the voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)
engine.setProperty('rate', 150)

mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

_, frame = cap.read()

h, w, c = frame.shape

img_counter = 0
analysisframe = ''
letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y']
class_labels = ['1', '10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'best of luck',  'i love you', 'unknow']
while True:
    _, frame = cap.read()

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        analysisframe = frame
        showframe = analysisframe
        cv2.imshow("Frame", showframe)
        framergbanalysis = cv2.cvtColor(analysisframe, cv2.COLOR_BGR2RGB)
        resultanalysis = hands.process(framergbanalysis)
        hand_landmarksanalysis = resultanalysis.multi_hand_landmarks
        cord_dict = {}
        if hand_landmarksanalysis:
            for handLMsanalysis in hand_landmarksanalysis:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                for lmanalysis in handLMsanalysis.landmark:
                    x, y = int(lmanalysis.x * w), int(lmanalysis.y * h)
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
                y_min -= 20
                y_max += 20
                x_min -= 20
                x_max += 20
                # print(y_min )
            cord_dict = {" y_min": y_min,
                         "y_max": y_max,
                         "x_min": x_min,
                         "x_max": x_max}

        analysisframe = cv2.cvtColor(analysisframe, cv2.COLOR_BGRA2RGB)
        analysisframe = analysisframe[y_min:y_max, x_min:x_max]
        analysisframe = cv2.resize(analysisframe, (64,64))
        analysisframe = analysisframe.reshape(1, 64, 64, 3)
        np.expand_dims(analysisframe, axis=0)
        # analysisframe = cv2.resize(analysisframe, (64, 64))
        result = model.predict(analysisframe)
        prediction = np.argmax(result)
        print(prediction)
        prediction_label = class_labels[prediction]
        print(prediction_label)
        # predarray = np.array(prediction[0])
        # print(predarray)
        # letter_prediction_dict = {letterpred[i]: predarray[i] for i in range(len(letterpred))}
        # print(letter_prediction_dict)
        # predarrayordered = sorted(predarray, reverse=True)
        # high1 = predarrayordered[0]
        # high2 = predarrayordered[1]
        # high3 = predarrayordered[2]
        # for key, value in letter_prediction_dict.items():
        #     if value == high1:
        #         print("Predicted Character 1: ", key)
        #         print('Confidence 1: ', 100 * value)
        #         t = threading.Thread(target=voice_message, args=(engine, key,))
        #         t.start()
        #     elif value == high2:
        #         print("Predicted Character 2: ", key)
        #         print('Confidence 2: ', 100 * value)
        #     elif value == high3:
        #         print("Predicted Character 3: ", key)
        #         print('Confidence 3: ', 100 * value)
        # time.sleep(5)

    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)
    hand_landmarks = result.multi_hand_landmarks
    if hand_landmarks:
        for handLMs in hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in handLMs.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            y_min -= 20
            y_max += 20
            x_min -= 20
            x_max += 20
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            mp_drawing.draw_landmarks(frame, handLMs, mphands.HAND_CONNECTIONS)
    cv2.imshow("Frame", frame)

# stopping the speech
# engine.endLoop()
engine.stop()
cap.release()
cv2.destroyAllWindows()
