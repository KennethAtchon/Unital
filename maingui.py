import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Unital')
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon('Unital.jpg'))

        self.setStyleSheet('background-color: #F0F8FF;')

        # Create widgets
        self.title_label = QLabel('Unital')
        self.title_label.setStyleSheet('background-color: #6495ED; color: white; font-size: 24px; padding: 10px;')
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setMaximumHeight(50)

        self.sidebar_button1 = QPushButton('Section 1')
        self.sidebar_button2 = QPushButton('Section 2')
        self.sidebar_button3 = QPushButton('Section 3')

        self.sidebar_button1.clicked.connect(self.on_sidebar_button1_click)
        self.sidebar_button2.clicked.connect(self.on_sidebar_button2_click)
        self.sidebar_button3.clicked.connect(self.on_sidebar_button3_click)

        # Create layout for the central widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.title_label)

        # Create a horizontal layout for the sidebar and content
        horizontal_layout = QHBoxLayout()

        # Set a maximum width for the sidebar layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.sidebar_button1)
        sidebar_layout.addWidget(self.sidebar_button2)
        sidebar_layout.addWidget(self.sidebar_button3)

        # Add even spacing between buttons
        sidebar_layout.addStretch()
        sidebar_layout.setSpacing(60)
        sidebar_layout.addStretch()

        sidebar_layout.setAlignment(QtCore.Qt.AlignTop)  # Align buttons at the top
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setStyleSheet('background-color: #6495ED; color: white;')  # Set background color
        sidebar_widget.setFixedWidth(150) 

        # Create a layout for the content to the right of the sidebar
        content_layout = QVBoxLayout()
        content_layout.addWidget(QLabel("Content to the right of the sidebar"))

        # Add sidebar and content layouts to the horizontal layout
        horizontal_layout.addWidget(sidebar_widget)
        horizontal_layout.addLayout(content_layout)

        # Add the horizontal layout to the main layout
        main_layout.addLayout(horizontal_layout)

        self.show()

    def on_sidebar_button1_click(self):
        self.title_label.setText('Section 1 clicked!')

    def on_sidebar_button2_click(self):
        self.title_label.setText('Section 2 clicked!')

    def on_sidebar_button3_click(self):
        self.title_label.setText('Section 3 clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    sys.exit(app.exec_())
