import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My GUI")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        # Top title
        title_label = QLabel("My GUI Title")
        title_label.setAlignment(Qt.AlignCenter)

        # Sidebar on the left
        sidebar_label = QLabel("Sidebar")
        sidebar_label.setAlignment(Qt.AlignCenter)
        sidebar_label.setStyleSheet("QLabel { background-color: lightgray; }")

        # Text on the right of the sidebar
        text_label = QLabel("Text Area")
        text_label.setAlignment(Qt.AlignCenter)

        # Layout
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addWidget(title_label)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(sidebar_label)
        horizontal_layout.addWidget(text_label)

        main_layout.addLayout(horizontal_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
