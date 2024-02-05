import cv2

from pyzbar import pyzbar
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    
    
    barcodes=pyzbar.decode(frame)
    for barcode in barcodes:
        x,y,w,h=barcode.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.putText(frame,barcode.data.decode("utf-8"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255))
    #cv2.imshow("",frame)
    cv2.imshow("th",frame)
    cv2.waitKey(1)
