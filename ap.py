import requests
import json
import subprocess

class DeviceInfo:
    def __init__(self):
        self.device_info = {}

    def get_device_info(self):
        # Get device name
        device_name = subprocess.check_output(["adb", "shell", "getprop", "ro.product.name"]).decode("utf-8")
        self.device_info["device_name"] = device_name

        # Get device model
        device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode("utf-8")
        self.device_info["device_model"] = device_model

        # Get device operating system
        device_os = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode("utf-8")
        self.device_info["device_os"] = device_os

        # Get device serial number
        device_serial = subprocess.check_output(["adb", "get-serialno"]).decode("utf-8")
        self.device_info["device_serial"] = device_serial

        return self.device_info


class Location:
    def __init__(self):
        self.location = {}

    def get_location(self):
        # Get device location using Google Maps API
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=your_api_key"
        response = requests.get(url)
        data = json.loads(response.content)

        # Get device latitude and longitude
        latitude = data["results"][0]["geometry"]["location"]["lat"]
        longitude = data["results"][0]["geometry"]["location"]["lng"]

        self.location["latitude"] = latitude
        self.location["longitude"] = longitude

        return self.location


class Webcam:
    def __init__(self):
        self.webcam = None

    def start_webcam(self):
        # Start the webcam
        self.webcam = subprocess.Popen(["adb", "shell", "am", "start", "-a", "android.media.action.STILL_IMAGE_CAMERA"])

    def stop_webcam(self):
        # Stop the webcam
        self.webcam.kill()

    def take_picture(self):
        # Take a picture using the webcam
        subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])

        # Pull the screenshot from the device
        subprocess.run(["adb", "pull", "/sdcard/screenshot.png", "."])

        # Delete the screenshot from the device
        subprocess.run(["adb", "shell", "rm", "/sdcard/screenshot.png"])


class Webcam:
    def __init__(self):
        self.webcam = None

    def start_webcam(self):
        # Start the webcam
        self.webcam = subprocess.Popen(["adb", "shell", "am", "start", "-a", "android.media.action.STILL_IMAGE_CAMERA"])

    def stop_webcam(self):
        # Stop the webcam
        self.webcam.kill()

    def take_picture(self):
        # Take a picture using the webcam
        subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])

        # Pull the screenshot from the device
        subprocess.run(["adb", "pull", "/sdcard/screenshot.png", "."])

        # Delete the screenshot from the device
        subprocess.run(["adb", "shell", "rm", "/sdcard/screenshot.png"])

    def record_video(self):
        # Record video using the webcam
        subprocess.run(["adb", "shell", "screenrecord", "-a", "/sdcard/video.mp4"])

        # Pull the video recording from the device
        subprocess.run(["adb", "pull", "/sdcard/video.mp4", "."])

        # Delete the video recording from the device
        subprocess.run(["adb", "shell", "rm", "/sdcard/video.mp4"])
class DeviceInfo:
    def __init__(self):
        self.device_info = {}

    def get_device_info(self):
        # Check if the device is connected
        if not subprocess.run(["adb", "devices"], capture_output=True).stdout:
            raise Exception("Device not connected")

        # Check if the device is authorized
        if not subprocess.run(["adb", "shell", "pm", "list", "packages", "-3"], capture_output=True).stdout:
            raise Exception("Device not authorized")

        # Get device name
        device_name = subprocess.check_output(["adb", "shell", "getprop", "ro.product.name"]).decode("utf-8")
        self.device_info["device_name"] = device_name

        # Get device model
        device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode("utf-8")
        self.device_info["device_model"] = device_model

        # Get device operating system
        device_os = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode("utf-8")
        self.device_info["device_os"] = device_os

        # Get device serial number
        device_serial = subprocess.check_output(["adb", "get-serialno"]).decode("utf-8")
        self.device_info["device_serial"] = device_serial

        return self.device_info









class Microphone:
    def __init__(self):
        self.microphone = None

    def start_microphone(self):
        # Start the microphone
        self.microphone = subprocess.Popen(["adb", "shell", "am", "start", "-a", "android.media.action.SOUND_RECORD"])

    def stop_microphone(self):
        # Stop the microphone
        self.microphone.kill()

    def record_audio(self):
        # Record audio using the microphone
        subprocess.run(["adb", "shell", "screenrecord", "-a", "/sdcard/audio.mp4"])

        # Pull the audio recording from the device
        subprocess.run(["adb", "pull", "/sdcard/audio.mp4", "."])

        # Delete the audio recording from the device
        subprocess.run(["adb", "shell", "rm", "/sdcard/audio.mp4"])


# Usage example

# Create a DeviceInfo object
device_info = DeviceInfo()

# Get device information
device_info_dict = device_info.get_device_info()

# Print device information
print(device_info_dict)

# Create a Location object
location = Location()

# Get device location
location_dict = location.get_location()

# Print device location
print(location_dict)

# Create a Webcam object
webcam = Webcam()

# Start the webcam
webcam.start_webcam()

# Take a picture
webcam.take_picture()

# Stop the webcam
webcam.stop_webcam()

# Create a Microphone object
microphone = Microphone()

# Start the microphone
microphone.start_microphone()

#
