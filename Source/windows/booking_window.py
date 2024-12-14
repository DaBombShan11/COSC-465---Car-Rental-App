from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class BookingWindow(QWidget):
    def __init__(self, brand, model, car_type, location, capacity):
        """
        Initialize the Booking Window with car details.
        :param brand: Brand of the car.
        :param model: Model of the car.
        :param car_type: Type of the car (e.g., Sedan, SUV).
        :param location: Location of the car.
        :param capacity: Seating capacity of the car.
        """
        super().__init__()
        self.brand = brand
        self.model = model
        self.car_type = car_type
        self.location = location
        self.capacity = capacity

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Booking Details")

        # Labels for car details
        brand_label = QLabel(f"Brand: {self.brand}")
        model_label = QLabel(f"Model: {self.model}")
        car_type_label = QLabel(f"Type: {self.car_type}")
        location_label = QLabel(f"Location: {self.location}")
        capacity_label = QLabel(f"Capacity: {self.capacity} seats")

        # Arrange labels in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(brand_label)
        layout.addWidget(model_label)
        layout.addWidget(car_type_label)
        layout.addWidget(location_label)
        layout.addWidget(capacity_label)

        self.setLayout(layout)
