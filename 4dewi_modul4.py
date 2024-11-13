from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        
        # Button
        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        # Window settings
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Belajar PyQt5")

# Application
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
