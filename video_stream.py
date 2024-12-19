import cv2

def start_video_stream():
    print("Starting video stream...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video!")
            break
        
        cv2.imshow("Live Video Stream", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping video stream...")
            break

    cap.release()
    cv2.destroyAllWindows()
