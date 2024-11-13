from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)

        # Membuat tombol
        self.button = QPushButton(self)
        self.button.setText("Button1")

        # Mengatur geometri jendela
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")

        # Menempatkan jendela di tengah layar
        cwa = self.frameGeometry()  # Mendapatkan geometri jendela
        cwc = QDesktopWidget().availableGeometry().center()  # Mendapatkan pusat layar
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())

        # Mengatur ukuran jendela agar tidak bisa diubah, menghilangkan frame, dan menyembunyikan tombol minimize
        self.setFixedSize(500, 500)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()