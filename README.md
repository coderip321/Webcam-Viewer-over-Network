📱 **Webcam Viewer Over Network** 💻

This project allows you to stream the webcam feed from your **mobile device** to your **PC** (laptop or desktop) over the same local Wi-Fi network using **Python**, **Flask**, and **OpenCV**. No mobile apps are required — simply configure the devices, and you'll be able to access your mobile webcam directly from your laptop!

---

## 🔧 **Requirements**:

- **Python 3.x**
- **Flask** – For serving the webcam feed via a web server.
- **OpenCV** – For processing and displaying the video feed.
- **Android or iOS Device** – The mobile device you want to stream the webcam from.
- **Wi-Fi Network** – Both the mobile device and the PC must be connected to the **same Wi-Fi network**.

---

## 📥 **Installation**:

### 1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/remote-webcam-viewer.git
   cd remote-webcam-viewer
   ```

### 2. **Install Dependencies**:
   Install the required Python packages by running the following:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Install OpenCV**:
   If you don't have OpenCV installed, you can install it using:
   ```bash
   pip install opencv-python
   ```

---

## 🚀 **Setup Instructions**:

### 1. **Find the Mobile Device's IP Address** 🌐

To get your mobile device's local IP address:

- **On Android**:
   - Open **Wi-Fi settings**.
   - Tap on the connected network and note down the **IP address** (e.g., `192.168.x.x`).

- **On iOS**:
   - Go to **Settings** → **Wi-Fi** → Tap the connected network → Note down the **IP address**.

### 2. **Configure `viewer.py`** 🖥️

In the `viewer.py` file, **replace the `mobile_ip` variable** with the IP address of your mobile device.

Find the following line in the code:
```python
mobile_ip = '192.168.x.x:8080'  # Replace with your mobile device's IP and port
```
Replace it with the IP address you obtained for your mobile device. For example:
```python
mobile_ip = '192.168.0.102:5000'  # Replace with your mobile device's IP and port
```

### 3. **Run the Python Server** 💻

Once you've configured the `viewer.py` file, run the server on your PC:
```bash
python app.py
```
This starts the Flask web server that serves the webcam feed.

### 4. **View the Webcam Feed** 👀

- Open a browser on your laptop or desktop and navigate to:
  ```http
  http://localhost:5000
  ```
- You should now see the live webcam feed from your mobile device.

---

## 🛠️ **Troubleshooting**:

- **Mobile IP Address**: Double-check that the mobile device's IP address is correctly entered into the `viewer.py` file and that both the mobile device and PC are connected to the **same Wi-Fi network**.
- **Connection Issues**: If you see `tcp://connection failed`, make sure both devices are on the **same local network** and verify the IP address again.
- **OpenCV Errors**: If OpenCV fails to display the webcam feed, ensure all required dependencies (`opencv-python`, `ffmpeg`, etc.) are properly installed.

---

## ⚡ **Features**:

- Stream the **live webcam feed** from your mobile device to your PC.
- No external apps are required on the mobile device.
- Simple setup using **Python**, **Flask**, and **OpenCV**.

---

## 📄 **Disclaimer**:

- This project is for **educational purposes only**. Please use it responsibly.
- You must have permission to access the webcam feed of any device you are streaming from.

---

## 🧑‍💻 **Contributors**:

- **Your Name** - Developer and Project Lead

---

## 📚 **License**:

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
