from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow, QPushButton, QVBoxLayout, QWidget
#from windows.login_window import LoginWindow
#from windows.signup_window import SignUpWindow
from windows.home_window import HomeWindow
from windows.logout_window import LogoutWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Customize window size
        self.resize(400, 700)  # Set the window size to 800x600 

        # Stacked widget to switch between windows
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create instances of each window
        #self.login_window = LoginWindow()
        #self.signup_window = SignUpWindow()
        self.home_window = HomeWindow()  # Pass the reference of MainWindow to HomeWindow
        self.logout_window = LogoutWindow()  # Pass the reference of MainWindow to LogoutWindow

        # Add windows to the stacked widget
        #self.stacked_widget.addWidget(self.login_window)
        #self.stacked_widget.addWidget(self.signup_window)
        self.stacked_widget.addWidget(self.home_window)
        self.stacked_widget.addWidget(self.logout_window)

        # Show the home window initially
        self.stacked_widget.setCurrentWidget(self.home_window)

        # Connect buttons in the home and logout windows to navigate
        self.home_window.logout_button.clicked.connect(self.show_logout)
        self.logout_window.logout_button.clicked.connect(self.show_home)
        self.logout_window.cancel_button.clicked.connect(self.show_home)

    def show_home(self):
        """Switch to the home window."""
        self.stacked_widget.setCurrentWidget(self.home_window)

    def show_logout(self):
        """Switch to the logout window."""
        self.stacked_widget.setCurrentWidget(self.logout_window)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
