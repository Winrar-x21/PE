import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мой крутецкий прокт")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        open_action = QAction("Open Image", self)
        open_action.triggered.connect(self.open_image)
        self.file_menu.addAction(open_action)

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
