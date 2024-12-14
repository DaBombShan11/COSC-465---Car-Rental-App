from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

class LogoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logout")

        # Layout
        layout = QVBoxLayout()

        #Logout confirmation message label
        self.label = QLabel("Are you sure you want to log out?")
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin: 20px;
        """)

        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Button to confirm logout
        self.logout_button = QPushButton("Yes, Log Out")
        layout.addWidget(self.logout_button)
        self.logout_button.setStyleSheet("""
            background-color: #3498db;
            font-size: 14px;
            color: white;
            border-radius: 15px;
            padding: 10px;
        """)

        # Button to cancel logout
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            background-color: red;
            font-size: 14px;
            color: white;
            border-radius: 15px;
            padding: 10px;
        """)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)
        # Apply dark background to the window itself
        self.setStyleSheet("""
            QMainWindow {
                color: #2c3e50;  /* Dark blue-gray background */
                color: #ecf0f1;  /* Light text color */
            }
        """)
