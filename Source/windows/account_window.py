from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class AccountDetailsWindow(QDialog):
    def __init__(self, name, email, phone, address, last_booking):
        super().__init__()
        self.setWindowTitle("Account Details")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        # Display user details
        layout.addWidget(QLabel(f"Name: {name}"))
        layout.addWidget(QLabel(f"Email: {email}"))
        layout.addWidget(QLabel(f"Phone: {phone}"))
        layout.addWidget(QLabel(f"Address: {address}"))
        layout.addWidget(QLabel(f"Last Booking: {last_booking}"))

        # Center alignment
        for i in range(layout.count()):
            layout.itemAt(i).widget().setAlignment(Qt.AlignLeft)

        self.setLayout(layout)
