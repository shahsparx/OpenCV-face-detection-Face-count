import numpy as np
import cv2
from Tkinter import *

#setting up the haar cascade classifiers from the opencv installation
face_cascade = cv2.CascadeClassifier('/home/shahsparx/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/shahsparx/opencv-3.2.0/data/haarcascades/haarcascade_eye.xml')

img = cv2.imread('2.JPG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search for faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#for each face, detect eyes
print len(faces);
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#this part is the Tkinter GUI for displaying face count
root = Tk(className="FaceCount")
FaceCount = Label(root,text="{noOfFaces} Faces detected!".format(noOfFaces=len(faces)),width=50,height=10)
FaceCount.pack()
root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()
root.mainloop()

#displaying the image
imgg = cv2.resize(img, (1366, 720)) 
cv2.imshow('img',imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()


