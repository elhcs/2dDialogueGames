# interface.py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog

class ImageLoaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.image_paths = ["", "", ""]

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Image Loader')

        self.load_buttons = [QPushButton(f'Load Character {i+1}', self) for i in range(2)]
        self.load_buttons.append(QPushButton(f'Load Location', self) )
        for i, button in enumerate(self.load_buttons):
            button.clicked.connect(lambda _, index=i: self.load_image(index))

        layout = QVBoxLayout()
        for button in self.load_buttons:
            layout.addWidget(button)

        self.setLayout(layout)

    def load_image(self, index):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.gif)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.image_paths[index] = file_path

            if all(self.image_paths):
                self.close()

    def get_selected_image_paths(self):
        return self.image_paths

if __name__ == '__main__':
    app = QApplication([])
    window = ImageLoaderApp()
    window.show()
    app.exec_()
