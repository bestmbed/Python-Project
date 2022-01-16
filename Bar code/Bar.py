from pathlib import WindowsPath
import sys
import datetime
import cv2
from pyzbar import pyzbar
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from Software_Bar import Ui_export_fileT

class Sof_Bar(QMainWindow, Ui_export_file) :
    def __init__(self):
        super(Sof_Bar, self).__init__()
        self.ui = Ui_export_file()
        self.ui.setupUi(self)
        self.ui.opencam.clicked.connect(self.Open_camera)
        

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            # 1
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 2
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6),
                        font, 2.0, (255, 255, 255), 1)
            # 3
            with open("barcode_result.txt", mode='w') as file:
                file.write("Recognized Barcode:" + barcode_info)

        return frame

    @pyqtSlot()
    def Open_camera(self):
            print('clicked')
            camera = cv2.VideoCapture(0)
            while(camera.isOpened()):
                ret, frame = camera.read()
                if ret == True:
                    self.displayImage(frame,0)
                    cv2.waitKey()
            # frame = self.read_barcodes(frame)
                else:
                    print ("not found")
            camera.release()
            cv2.destroyAllWindows()
                
        
    def displayImage(self, img,windows=0):
        qformat = QImage.Format_Indexed8
        print(img.shape)
        if len(img.shape) == 3:
            if(img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
                img = QImage(img, img.shape[1], img.shape[0],qformat)
                img = img.rgbSwapped()
                self.ui.Stream_video.setPixmap(QPixmap.fromImage(img))
                self.ui.Stream_video.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def main():
        # 1
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        # 2
        while ret:
            ret, frame = camera.read()
            frame = read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        # 3
        camera.release()
        cv2.destroyAllWindows()

        # 4
if __name__ == '__main__':
    # Sof_Bar.main()
    app = QApplication(sys.argv)
    Windows = Sof_Bar()
    # ui = Ui_export_file()
    # ui.setupUi(Windows)
    Windows.show()
    try:
        sys.exit(app.exec_())

    except:
        print('exited')
