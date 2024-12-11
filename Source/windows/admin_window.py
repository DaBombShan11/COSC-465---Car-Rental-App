from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QListWidget, QMessageBox

class AdminWindow(QWidget):
    def __init__(self, switch_to_home_callback):
        """
        Initialize the Admin Window with multiple user data, bookings, roles, and support comments.
        :param switch_to_home_callback: Function to switch to the Home Window.
        """
        super().__init__()
        self.switch_to_home_callback = switch_to_home_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Panel - User Management")

        # Title label
        title_label = QLabel("Admin Dashboard")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Users Table
        self.users_table = QTableWidget(self)
        self.users_table.setColumnCount(5)
        self.users_table.setHorizontalHeaderLabels(['Name', 'Email', 'Role', 'Bookings', 'Action'])
        self.users_table.setRowCount(4)  # Example of 4 users (can be dynamic)
        
        # Sample data for Users
        users_data = [
            ["Greg", "greg@example.com", "Admin", "2", "View Profile"],
            ["Alice", "alice@example.com", "Customer", "1", "View Profile"],
            ["Bob", "bob@example.com", "Customer", "0", "View Profile"],
            ["Eve", "eve@example.com", "Customer", "3", "View Profile"]
        ]

        for row, user in enumerate(users_data):
            for col, data in enumerate(user):
                self.users_table.setItem(row, col, QTableWidgetItem(data))

        # Add View Profile Button functionality for Admin
        self.users_table.cellClicked.connect(self.view_user_profile)

        # Bookings and Support Comments
        self.support_title = QLabel("Customer Support Comments")
        self.support_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")

        # Example of past support comments
        self.support_comments = QListWidget(self)
        self.support_comments.addItem("Greg - Resolved issue with car booking.")
        self.support_comments.addItem("Alice - Helped with payment issue.")
        self.support_comments.addItem("Bob - General inquiry about car options.")
        self.support_comments.addItem("Eve - Follow-up on booking status.")

        # Back to Home Window Button
        self.back_button = QPushButton("Switch to Home View")
        self.back_button.clicked.connect(self.switch_to_home)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.users_table)
        layout.addWidget(self.support_title)
        layout.addWidget(self.support_comments)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def view_user_profile(self, row, col):
        """
        This method will be triggered when an admin clicks a user row.
        It will show the user profile in a new window.
        """
        user_name = self.users_table.item(row, 0).text()
        user_email = self.users_table.item(row, 1).text()
        user_role = self.users_table.item(row, 2).text()
        user_bookings = self.users_table.item(row, 3).text()

        # For simplicity, let's just show the details in a message box
        profile_info = f"Name: {user_name}\nEmail: {user_email}\nRole: {user_role}\nBookings: {user_bookings}"
        
        QMessageBox.information(self, "User Profile", profile_info)
