from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Apply dark background to the main window itself
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;  /* Dark blue-gray background */
                color: #ecf0f1;  /* Light text color */
            }
        """)

        layout = QVBoxLayout()

        # Welcome label
        self.label = QLabel("Welcome to the App")
        layout.addWidget(self.label)

        # Button
        self.button = QPushButton("Go to Home")
        layout.addWidget(self.button)
