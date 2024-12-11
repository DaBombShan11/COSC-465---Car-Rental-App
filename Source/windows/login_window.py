from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")

        # Main layout
        layout = QVBoxLayout()

        # Add app name at the top with larger font
        self.app_name_label = QLabel("Zoom Mate")
        self.app_name_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #3498db; padding-top: 80px;")
        self.app_name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.app_name_label)

        # Add spacing between app name and login form
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Username/Email field
        self.username_label = QLabel("Username or Email:")
        self.username_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.username_field = QLineEdit(self)
        self.username_field.setPlaceholderText("Enter your username or email")
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_field)

        # Password field
        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)  # Hide password input
        self.password_field.setPlaceholderText("Enter your password")
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)

        # Error message label (hidden by default)
        self.error_label = QLabel("Invalid login credentials.")
        self.error_label.setStyleSheet("color: red; font-size: 14px;")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setVisible(False)  # Initially hidden
        layout.addWidget(self.error_label)

        # Add some spacing between error message and buttons
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Login button
        self.login_button = QPushButton("Login")
        layout.addWidget(self.login_button)

        # Sign-up button (optional)
        self.signup_button = QPushButton("Sign Up")
        layout.addWidget(self.signup_button)

        # Set the layout for the login window
        self.setLayout(layout)

        # Set overall window style
        self.setStyleSheet("""

            QLineEdit {
                background-color: gray;
                color: white;
                border: 1px solid #ecf0f1;
                padding: 10px;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }

            QLabel {
                font-size: 14px;
            }
        """)
