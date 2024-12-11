from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up Window")

        # Set the layout
        layout = QVBoxLayout()

        # Create labels and input fields for Sign-Up
        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.username_field = QLineEdit(self)
        self.username_field.setPlaceholderText("Enter your username")

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("Enter your password")
        self.password_field.setEchoMode(QLineEdit.Password)  # Mask the password input

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.confirm_password_field = QLineEdit(self)
        self.confirm_password_field.setPlaceholderText("Confirm your password")
        self.confirm_password_field.setEchoMode(QLineEdit.Password)

        self.email_label = QLabel("Email:")
        self.email_field = QLineEdit(self)
        self.email_field.setPlaceholderText("Enter your email address")

        # Create the Sign Up button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setStyleSheet("""
            background-color: #3498db;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
        """)

        # Add fields to the layout
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_field)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_field)
        layout.addWidget(self.signup_button)

        # Connect the Sign-Up button to a method
        self.signup_button.clicked.connect(self.signup)

    def signup(self):
        """Handle the sign-up process (validation and handling)."""
        username = self.username_field.text()
        password = self.password_field.text()
        confirm_password = self.confirm_password_field.text()
        email = self.email_field.text()

        if password != confirm_password:
            self.show_error("Passwords do not match.")
            return

        if not username or not password or not email:
            self.show_error("All fields must be filled.")
            return

        # Placeholder for saving the new user data (e.g., save to a database)
        print(f"User {username} signed up with email {email}.")

        # After successful sign-up, you can navigate to the next screen
        # self.navigate_to_home()  # Placeholder for home navigation

    def show_error(self, message):
        """Display an error message in a pop-up dialog."""
        from PyQt5.QtWidgets import QMessageBox
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()

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
