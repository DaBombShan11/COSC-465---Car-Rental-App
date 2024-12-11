from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class UserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("User Profile - Greg")
        
        # Create labels with dummy data
        name_label = QLabel("Name: Greg")
        email_label = QLabel("Email: greg@example.com")
        phone_label = QLabel("Phone: +1-555-1234")
        address_label = QLabel("Address: 123 Main Street, Hometown")
        membership_label = QLabel("Membership: Premium")

        # Arrange labels in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(email_label)
        layout.addWidget(phone_label)
        layout.addWidget(address_label)
        layout.addWidget(membership_label)

        self.setLayout(layout)
