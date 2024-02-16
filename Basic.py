import cv2
import face_recognition

imgOriginal = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgOriginal = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgOriginal)[0]
encodeOriginal = face_recognition.face_encodings(imgOriginal)[0]
cv2.rectangle(imgOriginal, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)

results = face_recognition.compare_faces([encodeOriginal], encodeTest)
faceDis = face_recognition.face_distance([encodeOriginal], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

cv2.imshow('Real Image', imgOriginal)
cv2.imshow('Test Image', imgTest)
cv2.waitKey(0)
