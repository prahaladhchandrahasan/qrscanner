from pyzbar.pyzbar import decode
import cv2
barcodeData=''
BLUR_VALUE = 3
vs = cv2.VideoCapture(2)
while True:

	
	ret,frame = vs.read()
	cv2.resize(frame,(1080,1080))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	gray = cv2.GaussianBlur(gray, (BLUR_VALUE, BLUR_VALUE), 0)
	img = cv2.imread("index.png",cv2.IMREAD_COLOR)
	img = cv2.resize(img,(1080,1080))
	barcodes = decode(gray)
	for barcode in barcodes:
		(x,y,w,h) = barcode.rect
		cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
		barcodeData = barcode.data.decode("utf-8")
		
	#cv2.imshow("barcode scanner",gray)
	cv2.imshow("payload drop",frame)


	if cv2.waitKey(1) & 0xFF ==ord('q') or barcodeData.isdigit():
		cv2.putText(img, barcodeData, (400,600),cv2.FONT_HERSHEY_SIMPLEX, 20, (255, 255, 255), 2)
		cv2.imshow("output",img)



	


vs.release()
cv2.destroyAllWindows()