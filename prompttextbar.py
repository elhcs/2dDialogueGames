import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        label = QLabel('Provide relevant information for dialogue generation:')
        self.input_field = QLineEdit(self)
        submit_button = QPushButton('Submit', self)
        submit_button.clicked.connect(self.submit_clicked)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.input_field)
        layout.addWidget(submit_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Input Window')
        self.show()

    def submit_clicked(self):
        # Function to handle submit button click
        input_text = self.input_field.text()
        print(f"Submitted Text: {input_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
