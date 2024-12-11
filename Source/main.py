from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
from windows.login_window import LoginWindow
from windows.signup_window import SignUpWindow
from windows.home_window import HomeWindow
from windows.logout_window import LogoutWindow
from windows.booking_window import BookingWindow
from windows.payment_window import PaymentWindow
from windows.user_window import UserWindow
from windows.admin_window import AdminWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Customize window size
        self.resize(400, 800)  # Set the window size to 400x800

        # Stacked widget to switch between windows
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create instances of each window
        self.login_window = LoginWindow()
        self.signup_window = SignUpWindow()
        self.home_window = HomeWindow()
        self.logout_window = LogoutWindow()
        self.payment_window = PaymentWindow()
        self.user_window = UserWindow()
        self.booking_window = BookingWindow(
            brand="Toyota",
            model="Camry",
            car_type="Sedan",
            location="Los Angeles",
            capacity=5
        )
        self.admin_window = AdminWindow(self.show_user)

        # Add windows to the stacked widget
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.home_window)
        self.stacked_widget.addWidget(self.logout_window)
        self.stacked_widget.addWidget(self.signup_window)
        self.stacked_widget.addWidget(self.payment_window)
        self.stacked_widget.addWidget(self.booking_window)
        self.stacked_widget.addWidget(self.user_window)
        self.stacked_widget.addWidget(self.admin_window)

        # Show the login window initially
        self.stacked_widget.setCurrentWidget(self.login_window)

        # Connect buttons in the home and logout windows to navigate
        self.login_window.login_button.clicked.connect(self.show_home)
        self.login_window.signup_button.clicked.connect(self.show_signup)
        self.home_window.logout_button.clicked.connect(self.show_logout)
        self.logout_window.logout_button.clicked.connect(self.show_login)
        self.logout_window.cancel_button.clicked.connect(self.show_home)

    def show_home(self):
        """Switch to the home window."""
        self.stacked_widget.setCurrentWidget(self.home_window)

    def show_login(self):
        """Switch to the login window."""
        self.stacked_widget.setCurrentWidget(self.login_window)
    
    def show_signup(self):
        """Switch to the signup window."""
        self.stacked_widget.setCurrentWidget(self.signup_window)

    def show_logout(self):
        """Switch to the logout window."""
        self.stacked_widget.setCurrentWidget(self.logout_window)

    def show_payment(self):
        """Switch to the payment window."""
        self.stacked_widget.setCurrentWidget(self.payment_window)

    def show_booking(self):
        """Switch to the booking window."""
        self.stacked_widget.setCurrentWidget(self.booking_window)
    
    def show_user(self):
        """Switch to the user window."""
        self.stacked_widget.setCurrentWidget(self.user_window)

    def show_admin(self):
        """Switch to the admin window."""
        self.stacked_widget.setCurrentWidget(self.admin_window)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
