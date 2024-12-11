# windows/home_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Window")
        
        # Apply dark background to the main window itself
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;  /* Dark blue-gray background */
                color: #ecf0f1;  /* Light text color */
            }
        """)

        # Layout
        layout = QVBoxLayout()

        # Welcome label
        self.label = QLabel("Welcome to the Home Page!")
        # Styling the welcome message with QSS
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin: 20px;
        """)
                
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Logout button
        self.logout_button = QPushButton("Log Out")
        self.logout_button.setStyleSheet("""
            background-color: #3498db;
            font-size: 14px;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)
