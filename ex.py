import cv2



def fun(recognizer):
	while True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the grayscale frame
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
		    # Recognize and label the faces
		for (x, y, w, h) in faces:
		    	# Recognize the face using the trained model
			label, confidence = recognizer.predict(gray[y:y + h, x:x + w])
		    	#print(confidence
			if confidence > 50:
		    		# Display the recognized label and confidence level
				cv2.putText(frame, label_name[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
		    		# Draw a rectangle around the face
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			else:
				print('Unrecognized')

		    # Display the frame with face recognition
			cv2.imshow('Recognize Faces', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
		        break