
import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
   model_selection=0, min_detection_confidence=0.4) as face_detection:

   while cap.isOpened():
      success, image = cap.read()
      if not success:
         print("Ignoring empty camera frame.")
         continue

      
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = face_detection.process(image)

     
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      if results.detections:
         for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

            faces = len(results.detections)
            cv2.putText(image, f'{faces}', (70, 100), cv2.FONT_HERSHEY_COMPLEX,
               3, (0, 255, 0), 4)
            
      print(len(results.detections))

      cv2.imshow('MediaPipe Face Detection', image)
      if cv2.waitKey(5) & 0xFF == 27:
         break
cap.release()