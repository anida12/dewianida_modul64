from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat widget pusat
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)

        # Membuat tombol-tombol
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")

        # Menambahkan tombol ke layout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        # Mengatur widget pusat sebagai widget utama jendela
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()