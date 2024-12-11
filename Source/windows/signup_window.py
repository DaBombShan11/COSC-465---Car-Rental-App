from PyQt5.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up Window")

        # Set up layout
        layout = QVBoxLayout()
        layout.setSpacing(0)  # Set the spacing between widgets to 5px

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)) 

        # Create labels and input fields for Sign-Up
        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.username_field = QLineEdit(self)
        self.username_field.setPlaceholderText("Enter your username")
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_field)

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("Enter your password")
        self.password_field.setEchoMode(QLineEdit.Password)  # Mask the password input
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.confirm_password_field = QLineEdit(self)
        self.confirm_password_field.setPlaceholderText("Confirm your password")
        self.confirm_password_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_field)

        self.email_label = QLabel("Email:")
        self.email_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.email_field = QLineEdit(self)
        self.email_field.setPlaceholderText("Enter your email address")
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_field)

        # Add Phone Number field
        self.phone_label = QLabel("Phone Number:")
        self.phone_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.phone_field = QLineEdit(self)
        self.phone_field.setPlaceholderText("Enter your phone number")
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_field)

        # Add Address field
        self.address_label = QLabel("Address:")
        self.address_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.address_field = QLineEdit(self)
        self.address_field.setPlaceholderText("Enter your address")
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_field)

        layout.addItem(QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)) 
        
        # Create the Sign Up button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setStyleSheet("""
            background-color: #3498db;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
        """)
        layout.addWidget(self.signup_button)

        # Center the widgets
        self.setLayout(layout)

        # Connect the Sign-Up button to a method
        self.signup_button.clicked.connect(self.signup)

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
                margin: 0;
            }        
        """)

    def signup(self):
        """Handle the sign-up process (validation and handling)."""
        username = self.username_field.text()
        password = self.password_field.text()
        confirm_password = self.confirm_password_field.text()
        email = self.email_field.text()
        phone = self.phone_field.text()
        address = self.address_field.text()

        if password != confirm_password:
            self.show_error("Passwords do not match.")
            return

        if not username or not password or not email or not phone or not address:
            self.show_error("All fields must be filled.")
            return

        # Placeholder for saving the new user data (e.g., save to a database)
        print(f"User {username} signed up with email {email}, phone {phone}, and address {address}.")

        # After successful sign-up, you can navigate to the next screen
        # self.navigate_to_home()  # Placeholder for home navigation

    def show_error(self, message):
        """Display an error message in a pop-up dialog."""
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
