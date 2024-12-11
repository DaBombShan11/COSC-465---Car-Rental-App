from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class SupportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Support")

        # Main layout
        layout = QVBoxLayout()

        # Title for the support page
        self.support_label = QLabel("Customer Support")
        self.support_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #3498db; padding-top: 40px;")
        self.support_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.support_label)

        # Add a spacer for spacing
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Description field
        self.description_label = QLabel("Describe your issue:")
        self.description_label.setStyleSheet("font-size: 14px; color: #3498db;")
        self.description_field = QTextEdit(self)
        self.description_field.setPlaceholderText("Please describe your issue or request here...")
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_field)

        # Submit button
        self.submit_button = QPushButton("Submit Request")
        layout.addWidget(self.submit_button)

        # Success message (hidden by default)
        self.success_label = QLabel("Your request has been submitted successfully.")
        self.success_label.setStyleSheet("color: green; font-size: 14px;")
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label.setVisible(False)
        layout.addWidget(self.success_label)

        # Set the layout for the support window
        self.setLayout(layout)

        # Set overall window style
        self.setStyleSheet("""
            QTextEdit {
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
        
        # Connect the submit button to submit logic
        self.submit_button.clicked.connect(self.submit_request)

    def submit_request(self):
        """Handle the support request submission."""
        # For simplicity, we can just clear the text and show a success message
        description = self.description_field.toPlainText()
        if description:
            self.success_label.setVisible(True)  # Show success message
            self.description_field.clear()  # Clear the description field after submission
        else:
            self.success_label.setText("Please provide a description of your issue.")
            self.success_label.setStyleSheet("color: red; font-size: 14px;")
            self.success_label.setVisible(True)  # Show error message if description is empty
