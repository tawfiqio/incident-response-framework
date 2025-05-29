import os

def check_usb_devices():
    usb_devices = os.popen("lsusb").read()
    print("🔌 Connected USB Devices:\n", usb_devices)

if __name__ == "__main__":
    check_usb_devices()
