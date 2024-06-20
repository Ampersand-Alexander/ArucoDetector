import time
import picamera

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set camera resolution (optional)
    camera.resolution = (640, 480)

    # Start a preview on the screen
    camera.start_preview()

    # Allow some time for the camera to warm up
    time.sleep(5)

    # Capture an image and save it to a file (optional)
    camera.capture('preview_image.jpg')

    # Keep the preview running until user interrupts
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop the preview
        camera.stop_preview()
