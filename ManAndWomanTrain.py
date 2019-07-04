import cv2
import numpy as np
import pickle
import os
from sklearn import svm

Face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

L = list()
Big = list()
#images = list()
NewB = list()
hog = cv2.HOGDescriptor()
path = 'D:\\College\\Compuer Vision\\Project\\Dataset\\manwomandetection\\train\\TrainHahahaha\\'
images = os.listdir(path)
for j in images:
    image = cv2.imread(path+j)

    Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    Faces = Face_xml.detectMultiScale(Gray, 1.1, 3)

    for (x, y, w, h) in Faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (150, 60, 255), 2)

        GrayBorder = Gray[y:y + h, x:x + w]
        ColorBorder = image[y:y + h, x:x + w]
        Cropped=image[y:y + h, x:x + w]
        resized_image = cv2.resize(Cropped, (64, 128))

    # c=0
    # while(c!=''):
    #     if c""
    if 'man' in j:
        L.append(0)
    if 'bnat' in j:
        L.append(1)

    h = hog.compute(resized_image)
    Big.append(h)
    print (h.mean(), L[-1])

BN = np.array(Big, np.float32)
LN = np.array(L, np.int)
print(BN.shape)
print(LN.shape)
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)


svm.train(BN, cv2.ml.ROW_SAMPLE, LN)

svm.save('gender.dat')
#filename = 'SVModel.sav'
#pickle.dump(svm, open(filename, 'wb'))

