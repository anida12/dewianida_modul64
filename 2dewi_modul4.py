from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()

# Label menggunakan cara 2
label = QLabel(window)
label.setText("Label1")
label.move(200, 0)

# Button menggunakan cara 2
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()
