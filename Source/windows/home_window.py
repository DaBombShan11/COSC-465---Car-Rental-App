from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QGridLayout, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from windows.support_window import SupportWindow  # Import SupportWindow
from windows.booking_window import BookingWindow  # Import BookingWindow

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Window")
        
        # Test data for cars
        self.cars = [
            {"brand": "Toyota", "model": "Corolla", "type": "Sedan", "location": "New York", "capacity": 5},
            {"brand": "Ford", "model": "Mustang", "type": "Coupe", "location": "Los Angeles", "capacity": 4},
            {"brand": "Honda", "model": "Civic", "type": "Sedan", "location": "Chicago", "capacity": 5},
            {"brand": "Tesla", "model": "Model X", "type": "SUV", "location": "San Francisco", "capacity": 7},
        ]
        
        # Layout
        layout = QVBoxLayout()

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search for cars, bookings, etc...")
        self.search_button = QPushButton(QIcon("search_icon.png"), "Search")
        self.search_button.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border-radius: 5px;")

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Filter options
        self.filter_brand = QLineEdit(self)
        self.filter_brand.setPlaceholderText("Filter by brand (e.g., Toyota)")

        self.filter_type = QLineEdit(self)
        self.filter_type.setPlaceholderText("Filter by type (e.g., Sedan)")

        self.filter_location = QLineEdit(self)
        self.filter_location.setPlaceholderText("Filter by location (e.g., New York)")

        self.filter_capacity = QLineEdit(self)
        self.filter_capacity.setPlaceholderText("Filter by capacity (e.g., 5)")

        filter_layout = QVBoxLayout()
        filter_layout.addWidget(self.filter_brand)
        filter_layout.addWidget(self.filter_type)
        filter_layout.addWidget(self.filter_location)
        filter_layout.addWidget(self.filter_capacity)

        layout.addLayout(filter_layout)

        # Results list
        self.results_list = QListWidget(self)
        layout.addWidget(self.results_list)

        self.search_button.clicked.connect(self.perform_search)

        # Welcome label
        self.label = QLabel("Welcome to the Home Page!")
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #ecf0f1;
            text-align: center;
            margin: 20px;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Logout button
        self.logout_button = QPushButton("Log Out")
        self.logout_button.setStyleSheet("""
            background-color: #3498db;
            font-size: 14px;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.logout_button)

        # Support button
        self.support_button = QPushButton("Customer Support")
        self.support_button.setStyleSheet("""
            background-color: #2ecc71;
            font-size: 14px;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.support_button)
        self.support_button.clicked.connect(self.open_support_window)

        # Connect the result list item clicked to show the booking window
        self.results_list.itemClicked.connect(self.open_booking_window)

        self.setLayout(layout)

    def perform_search(self):
        query = self.search_bar.text().lower()
        brand_filter = self.filter_brand.text().lower()
        type_filter = self.filter_type.text().lower()
        location_filter = self.filter_location.text().lower()
        capacity_filter = self.filter_capacity.text()

        capacity_filter = int(capacity_filter) if capacity_filter.isdigit() else None

        filtered_cars = [
            car for car in self.cars
            if (query in car["brand"].lower() or query in car["model"].lower()) and
            (not brand_filter or brand_filter in car["brand"].lower()) and
            (not type_filter or type_filter in car["type"].lower()) and
            (not location_filter or location_filter in car["location"].lower()) and
            (not capacity_filter or car["capacity"] == capacity_filter)
        ]

        self.results_list.clear()
        if filtered_cars:
            for car in filtered_cars:
                self.results_list.addItem(f'{car["brand"]} {car["model"]} - {car["type"]} - '
                                          f'{car["location"]} - Capacity: {car["capacity"]}')
        else:
            self.results_list.addItem("No cars match your criteria.")

    def open_booking_window(self):
        selected_car = self.results_list.currentItem().text()
        details = selected_car.split(" - ")
        print(details)
        print(details[0].split(" ")[0])
        # Initialize variables to store the extracted details
        brand = model = car_type = location = capacity = None

        # Loop through the details and extract information
        for detail in details:
            brand = details[0].split(" ")[0]
            model = details[0].split(" ")[1]
            car_type = details[1]
            location = details[2]
            if "Capacity:" in detail:
                capacity = int(detail.split("Capacity: ")[1])

        print(f"Booking for {brand} {model} - {car_type} - {location} - Capacity: {capacity}")

        # Now pass the correct values to the booking window
        self.booking_window = BookingWindow(brand, model, car_type, location, capacity)
        self.booking_window.show()




    def open_support_window(self):
        self.support_window = SupportWindow()
        self.support_window.show()
