from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFormLayout, QPushButton, QMessageBox

class PaymentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payment Processing")

        layout = QVBoxLayout()

        # Payment form layout
        self.payment_form = QFormLayout()
        self.card_number_input = QLineEdit(self)
        self.card_number_input.setPlaceholderText("Enter Card Number")
        self.expiry_date_input = QLineEdit(self)
        self.expiry_date_input.setPlaceholderText("Enter Expiration Date (MM/YY)")
        self.cvv_input = QLineEdit(self)
        self.cvv_input.setPlaceholderText("Enter CVV")
        self.cvv_input.setEchoMode(QLineEdit.Password)

        self.payment_form.addRow("Card Number:", self.card_number_input)
        self.payment_form.addRow("Expiration Date:", self.expiry_date_input)
        self.payment_form.addRow("CVV:", self.cvv_input)

        layout.addLayout(self.payment_form)

        self.pay_button = QPushButton("Process Payment")
        self.pay_button.setStyleSheet("""
            background-color: #3498db;
            font-size: 14px;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.pay_button)

        self.pay_button.clicked.connect(self.process_payment)

        self.setLayout(layout)

    def process_payment(self):
        card_number = self.card_number_input.text()
        expiry_date = self.expiry_date_input.text()
        cvv = self.cvv_input.text()

        if not card_number or not expiry_date or not cvv:
            QMessageBox.warning(self, "Missing Information", "Please fill in all payment details!")
            return

        QMessageBox.information(self, "Payment Successful", "Your payment has been processed successfully!")
        self.close()
