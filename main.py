import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QFileDialog, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from math import pi, sin, cos

W = 600

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.color = (0, 0, 0)
        self.setGeometry(200, 200, 300 + W, W)
        self.setWindowTitle('Замечательные кривые')
        self.combo = QComboBox(self)
        self.combo.resize(180, 30)
        self.combo.move(20, 30)
        self.combo.addItems(['Полярная роза',
                             'Кардиоида',
                             'Сердце'])
        self.lbs = QLabel(self)
        self.lbs.setText("N")
        self.lbs.move(20, 95)
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.valueChanged.connect(self.value_change)
        self.slider.setMaximum(10)
        self.slider.setMinimum(1)
        self.slider.resize(150, 30)
        self.slider.setValue(5)
        self.slider.move(50, 95)

    def value_change(self):
        self.repaint()
        
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(QColor("red")))
        if self.combo.currentText() == 'Кардиоида':
            self.draw_pascal(qp)
        elif self.combo.currentText() == 'Полярная роза':
            self.draw_rose(qp)
        elif self.combo.currentText() == 'Сердце':
            self.draw_hearth(qp)
        qp.end()
  
    def draw_pascal(self, qp, r=100):
        n = self.slider.value() * 3
        xc, yc = W, W // 3
        t = 0
        step = 1 / n
        x = round(2 * r * sin(t) + r * sin(t * 2)) + xc
        y = round(2 * r * cos(t) + r * cos(t * 2)) + yc
        while t <= 2 * pi:
            t += step
            x1 = round(2 * r * sin(t) + r * sin(t * 2)) + xc
            y1 = round(2 * r * cos(t) + r * cos(t * 2)) + yc
            qp.drawLine(x, y, x1, y1)
            x, y = x1, y1
           
    def draw_rose(self, qp, a=200, k=3):
        k = self.slider.value()
        xc, yc = W // 2 + 300, W // 2
        t = 0
        step = 0.01
        p = a * sin(k * t)
        x = round(p * cos(t)) + xc
        y = round(p * sin(t)) + yc
        while t <= 2 * pi:
            t += step
            p = a * sin(k * t)
            x1 = round(p * cos(t)) + xc
            y1 = round(p * sin(t)) + yc
            qp.drawLine(x, y, x1, y1)
            x, y = x1, y1

    def draw_hearth(self, qp, a=100):
        xc, yc = W // 2 + 300, W // 4
        step = 0.01
        t = pi - step
        p = a * ((sin(t) * (abs(cos(t))) ** 0.5) / (sin(t) + 7/5) - 2 * sin(t) + 2)
        x = round(p * cos(t)) + xc
        y = yc - round(p * sin(t)) + yc
        while t > -pi:
            t -= step
            p = a * ((sin(t) * (abs(cos(t))) ** 0.5) / (sin(t) + 7 / 5) - 2 * sin(t) + 2)
            x1 = round(p * cos(t)) + xc
            y1 = yc - round(p * sin(t))
            qp.drawLine(x, y, x1, y1)
            x, y = x1, y1

            
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
