from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("Main PyQt Widgets")
window.setGeometry(200, 200, 350, 500)

layout = QVBoxLayout()

label = QLabel("This is a QLabel")
layout.addWidget(label)

input_box = QLineEdit()
input_box.setPlaceholderText("QLineEdit - Enter text")
layout.addWidget(input_box)

text_area = QTextEdit()
text_area.setPlaceholderText("QTextEdit - Multi-line text")
layout.addWidget(text_area)

button = QPushButton("QPushButton")
layout.addWidget(button)

check = QCheckBox("QCheckBox - I agree")
layout.addWidget(check)

radio = QRadioButton("QRadioButton Option")
layout.addWidget(radio)

combo = QComboBox()
combo.addItems(["Option 1", "Option 2", "Option 3"])
layout.addWidget(combo)

slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
layout.addWidget(slider)

spin = QSpinBox()
spin.setRange(0, 50)
layout.addWidget(spin)

progress = QProgressBar()
progress.setValue(50)
layout.addWidget(progress)

window.setLayout(layout)
window.show()
app.exec()
