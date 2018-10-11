import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import time
from AudioIO import listen, speak
from settings import veronica_notify
name=""
faces=[]
i=1
c=0
labels=[]

face_recognizer = cv2.face.LBPHFaceRecognizer_create()


def test():
    global face_recognizer
    faces,labels=prepare_training_data()
    j=1
    while j<len(faces):
        s=str(faces[j])
        if s[1][0]=="0":
#print (str(j))
            del faces[j]
            j=j-1
        j=j+1
   # except:
      #  print("done")
    print(len(faces))
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    labels=[1]*len(faces)
    face_recognizer.train(faces, np.array(labels))
    cam=cv2.VideoCapture(0)
    time.sleep(2)
    r,img=cam.read()
    del(cam)
    cv2.imwrite("/home/anmol/Desktop/test/t.jpg",img)
    predict()
    

def train():
    speak("training")
    veronica_notify("Training")
    cam=cv2.VideoCapture(0)
    #time.sleep(10)
    for i in range(20):
        r,img=cam.read()
        cv2.imwrite("/home/anmol/Desktop/s2/"+str(i)+".jpg",img)
        time.sleep(1)
    del(cam)
    #exit()

def detect_face(img):
#convert the test image to gray scale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#load OpenCV face detector, I am using LBP which is fast
#there is also a more accurate but slow: Haar classifier
    face_cascade = cv2.CascadeClassifier('/home/anmol/Desktop/lbpcascade_frontalface_improved.xml')
    
#let's detect multiscale images(some images may be closer to camera than others)
#result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
 
#if no faces are detected then return original img
    if (len(faces) == 0):
        return np.zeros((2,2),dtype='int')
    (x, y, w, h) = faces[0]
 
#return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data():
        """dirs = os.listdir(data_folder_path)
        for dir_name in dirs:
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name"""
        faces = []
        label=1
        labels = []
        subject_images_names = os.listdir("/home/anmol/Desktop/s2")
        for image_name in subject_images_names:
            image_path = "/home/anmol/Desktop/s2/" + image_name
            image = cv2.imread(image_path)
            face, rect = detect_face(image)
            faces.append(face)
            labels.append(label)
            """cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.destroyAllWindows()"""
        return faces, labels

def predict():
    img=cv2.imread("/home/anmol/Desktop/test/t.jpg")
    face, rect = detect_face(img)
    label,s= face_recognizer.predict(face)
    print("welcome",name)
    veronica_notify("welcome" + name)
    speak("welcome " + name)
    exit()


# name=input("input your name")
# f=input("1. login/n2.train")
# if(f=="1"):
# 	test()
# if(f=="2"):
#     train()
    
