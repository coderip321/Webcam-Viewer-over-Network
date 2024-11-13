import cv2

def view_stream(mobile_ip):
    stream_url = f"http://{mobile_ip}:5000/video_feed"
    cap = cv2.VideoCapture(stream_url)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame. Check the mobile server.")
            break

        cv2.imshow("Mobile Webcam Stream", frame)

        # Press 'q' to exit the viewer
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace with your mobile device's IP address on the network
    mobile_ip = "192.168.0.102:5000"  # Replace with the actual IP
    view_stream(mobile_ip)
