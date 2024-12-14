from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from .payment_window import PaymentWindow  # Import the PaymentWindow class from payment_window.py

class BookingWindow(QWidget):
    def __init__(self, brand, model, car_type, location, capacity):
        super().__init__()
        self.setWindowTitle("Booking Window")

        layout = QVBoxLayout()
        car_details_text = (f"Car Details:\n"
                            f"Brand: {brand}\n"
                            f"Model: {model}\n"
                            f"Type: {car_type}\n"
                            f"Location: {location}\n"
                            f"Capacity: {capacity}")
        
        self.car_details_label = QLabel(car_details_text)
        self.car_details_label.setWordWrap(True)
        layout.addWidget(self.car_details_label)

        self.book_button = QPushButton("Confirm Booking")
        self.book_button.setStyleSheet("""
            background-color: #3498db;
            font-size: 14px;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.book_button)

        self.book_button.clicked.connect(self.confirm_booking)

        self.setLayout(layout)

    def confirm_booking(self):
        # Booking confirmation
        QMessageBox.information(self, "Booking Confirmed", "Your booking has been confirmed. Please proceed with payment.")
        
        # Open Payment Window
        self.payment_window = PaymentWindow()  # Open the PaymentWindow
        self.payment_window.show()

        # Close the booking window
        self.close()
