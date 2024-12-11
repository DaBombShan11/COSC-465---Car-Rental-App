from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

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

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search for cars, bookings, etc...")
        self.search_button = QPushButton(QIcon("search_icon.png"), "Search")  # Use an icon for the search button
        self.search_button.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border-radius: 5px;")

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

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
