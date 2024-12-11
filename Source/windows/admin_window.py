from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout

class AdminWindow(QWidget):
    def __init__(self, switch_to_user_callback):
        """
        Initialize the Admin Window.
        :param switch_to_user_callback: Function to switch to the User Window.
        """
        super().__init__()
        self.switch_to_user_callback = switch_to_user_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Panel - User Management")

        # Title label
        title_label = QLabel("User Accounts")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # List of dummy user accounts
        user_list = QListWidget()
        user_list.addItem("Greg - greg@example.com")
        user_list.addItem("Alice - alice@example.com")
        user_list.addItem("Bob - bob@example.com")
        user_list.addItem("Eve - eve@example.com")

        # Button to view Greg's profile
        view_greg_button = QPushButton("View Greg's Profile")
        view_greg_button.clicked.connect(self.switch_to_user_callback)

        # Layouts
        list_layout = QVBoxLayout()
        list_layout.addWidget(title_label)
        list_layout.addWidget(user_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(view_greg_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(list_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
