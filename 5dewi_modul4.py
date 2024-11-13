from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

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
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        
        # Center the window on the screen
        cwa = self.frameGeometry()  # Get main window size
        screen_center = QDesktopWidget().availableGeometry().center()  # Get screen center
        cwa.moveCenter(screen_center)  # Move window to screen center
        self.move(cwa.topLeft())  # Move top left of window to center

# Application
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
