import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt

# Database connection
conn = sqlite3.connect('car_rental_app.db')
cursor = conn.cursor()

# Create Users Table if not already created
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    license TEXT NOT NULL,
    age INTEGER NOT NULL,
    document_path TEXT
);
''')
conn.commit()

# Function to insert a new user into the database
def create_user(name, email, password_hash, license, age, document_path):
    cursor.execute('''
    INSERT INTO Users (name, email, password_hash, license, age, document_path)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, email, password_hash, license, age, document_path))
    conn.commit()

# PyQt application
class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.setWindowTitle('User Registration')
        self.setGeometry(100, 100, 300, 300)

        # Create layout
        layout = QVBoxLayout()

        # Name Field
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Email Field
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Password Field
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Driver's License Field
        self.license_label = QLabel('Driver\'s License:')
        self.license_input = QLineEdit()
        layout.addWidget(self.license_label)
        layout.addWidget(self.license_input)

        # Age Field
        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        # Document Upload Button
        self.document_label = QLabel('Upload Driver\'s License Image:')
        self.document_button = QPushButton('Choose File')
        self.document_button.clicked.connect(self.upload_document)
        layout.addWidget(self.document_label)
        layout.addWidget(self.document_button)

        # Submit Button
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.register_user)
        layout.addWidget(self.submit_button)

        # Set the layout
        self.setLayout(layout)

    def upload_document(self):
        # Open file dialog to select document
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.document_path = file_path

    def register_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()  # In real-world applications, password should be hashed
        license = self.license_input.text()
        age = int(self.age_input.text())

        # Validate input
        if not name or not email or not password or not license or not age:
            print("Please fill in all fields")
            return

        # Insert into database
        create_user(name, email, password, license, age, self.document_path)

        # Success message
        print("User registered successfully!")

        # Optionally, clear fields
        self.name_input.clear()
        self.email_input.clear()
        self.password_input.clear()
        self.license_input.clear()
        self.age_input.clear()

# Start the application
def main():
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
