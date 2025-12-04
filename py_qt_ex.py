from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# Simple fixed conversion rates
USD_TO_INR = 83.0
INR_TO_USD = 1 / USD_TO_INR

app = QApplication([])

window = QWidget()
window.setWindowTitle("Currency Converter")
window.setGeometry(200, 200, 300, 150)

label1 = QLabel("Amount:", window)
label1.move(20, 20)

input_box = QLineEdit(window)
input_box.move(100, 20)

result_label = QLabel("", window)
result_label.move(20, 100)

def convert_to_inr():
    try:
        amount = float(input_box.text())
        result = amount * USD_TO_INR
        result_label.setText(f"INR: {result:.2f}")
    except:
        result_label.setText("Invalid input")

def convert_to_usd():
    try:
        amount = float(input_box.text())
        result = amount * INR_TO_USD
        result_label.setText(f"USD: {result:.2f}")
    except:
        result_label.setText("Invalid input")

btn1 = QPushButton("USD ➜ INR", window)
btn1.move(20, 60)
btn1.clicked.connect(convert_to_inr)

btn2 = QPushButton("INR ➜ USD", window)
btn2.move(150, 60)
btn2.clicked.connect(convert_to_usd)

window.show()
app.exec()
