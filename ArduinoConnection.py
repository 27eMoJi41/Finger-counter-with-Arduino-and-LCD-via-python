import serial.tools.list_ports
import FingerCount as fc
import cv2
import keyboard
def main():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []

    for port in ports:
        portsList.append(str(port))
        print(str(port))

    com = input("Select port number:")
    for i in range(len(portsList)):
        if portsList[i].startswith("COM"+com):
            use = "COM"+com
            print("Using "+use)

    serialInst.baudrate = 9600
    serialInst.port = use
    serialInst.open()

    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        msg,_ = fc.FingerCount.counter(fc,img)
        serialInst.write(str(msg).encode('utf-8'))

        if keyboard.is_pressed("q"):
            exit()

if __name__ == "__main__":
    main()