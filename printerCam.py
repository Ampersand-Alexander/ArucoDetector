import cv2
import time
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
output_pin = 17  # Example GPIO pin, adjust as needed
GPIO.setup(output_pin, GPIO.OUT)

# Initialize OpenCV ArUco detector
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()
last_detection_time = time.time()

# Open the camera (adjust the camera index as needed, 0 is usually the webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        # Detect markers
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

        # Check if markers are found
        if ids is not None and len(ids) > 0:
            last_detection_time = time.time()
            # Here you could perform additional actions if markers are found

        # Check time since last detection
        if time.time() - last_detection_time > 5:
            # No marker detected for 5 seconds, send signal
            GPIO.output(output_pin, GPIO.HIGH)
        else:
            GPIO.output(output_pin, GPIO.LOW)

        # Display the frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
