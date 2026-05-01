import csv
from datetime import datetime
from PyQt6.QtWidgets import *
from gui import *


class ShiftTracker(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_clock_in.clicked.connect(self.clock_in)
        self.button_clock_out.clicked.connect(self.clock_out)
        self.button_clear.clicked.connect(self.clear_form)

    def clock_in(self):
        user_id = self.input_user_id.text()

        if user_id == '':
            QMessageBox.warning(self, "Error", "User ID is required")
            return

        self.label_status.setText(f"User {user_id} clocked in")

    def clock_out(self):
        user_id = self.input_user_id.text()
        notes = self.input_notes.text()

        if user_id == '':
            QMessageBox.warning(self, "Error", "User ID is required")
            return

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("shifts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user_id, time, notes])

        self.label_status.setText(f"User {user_id} clocked out and saved")

    def clear_form(self):
        self.input_user_id.clear()
        self.input_notes.clear()
