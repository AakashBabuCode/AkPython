import cv2
import winsound
import pyttsx3

engine = pyttsx3.init()
cam = cv2.VideoCapture(0)
detect = cv2.CascadeClassifier("C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
count = 0
while True:
    ret,frame = cam.read()
    faces = detect.detectMultiScale(frame,1.3,5)
    for x,y,w,h in faces:
        count = count+1
        name = "C:\\Users\\ELCOT\AppData\\Local\\Programs\\Python\\Python39\\images\\faces"+str(count)+".jpg"
        print("Images creating..")
        cv2.imwrite((name),frame[y:y+h,x:x+y])
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),3)
        cv2.rectangle(frame, (x,y-40), (x+w,y), (0,0,255),-1)
        cv2.putText(frame, "mask can't identify", (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255),1)
        engine.say("sir, wear your mask please, keep safe, sir")
        engine.runAndWait()
    cv2.imshow("Aakash", frame)
    cv2.waitKey(50)
    if count>500:
            break
cv2.waitKey(1)
cam.release()
cv2.destroyAllWindows()