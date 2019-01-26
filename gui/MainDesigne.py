from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class ClickLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)



class Window(QWidget):


    def __init__(self):
        self.checker = False

        QWidget.__init__(self)
        self.resize(600, 600)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        # database create

        ##self.db = Db()
        #db.create_table()


        self.mainLayout()

    def on_button_Send_clicked(self):
        self.question = self.lineedit.text()
        print(self.question)
        self.checker=True
        self.mainLayout()


    def mainLayout(self):
        layout = QVBoxLayout()

        button_Exit = QPushButton("Exit")
        button_Exit.setFont(QFont('Arial', 15))
        ##buttonBack.clicked.connect(self.on_buttonBackNoteEntry_clicked)

        labelTextTitle = QLabel("Bangla Intelligent ChatBot")
        labelTextTitle.setFont(QFont('Arial', 18))

        self.plaintextedit = QPlainTextEdit()
        self.plaintextedit.setFont(QFont('Arial', 15))
        # self.plaintextedit.insertPlainText("")
        if(self.checker):
            self.plaintextedit.insertPlainText(self.question)
        else:
            self.plaintextedit.setPlaceholderText("তুমার উত্তর এইখানে থাকবে")
        # textedit = QTextEdit()
        # textedit.setPlaceholderText("This is some placeholder text.")

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont('Arial', 15))
        self.lineedit.resize(300, 500)
        self.lineedit.setPlaceholderText("তুমার প্রশ্ন এইখানে লিখো")
        # self.lineedit.move(100, 100)
        ##self.lineedit.returnPressed.connect(self.return_pressed_lineedit)
        self.lineedit.setAlignment(Qt.AlignHCenter)


        button_Send = QPushButton("Send")
        button_Send.setFont(QFont('Arial', 15))
        button_Send.clicked.connect(self.on_button_Send_clicked)

        layout.addWidget(labelTextTitle)
        layout.addWidget(self.plaintextedit)
        layout.addWidget(self.lineedit)
        layout.addWidget(button_Send)
        layout.addWidget(button_Exit)

        self.setLayout(layout)





 # for layout clear
    def setLayout(self, layout):
        self.clearLayout()
        QWidget.setLayout(self, layout)

    def clearLayout(self):
        if self.layout() is not None:
            old_layout = self.layout()
            for i in reversed(range(old_layout.count())):
                old_layout.itemAt(i).widget().setParent(None)
            import sip
            sip.delete(old_layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())
