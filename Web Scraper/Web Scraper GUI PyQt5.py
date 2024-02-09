import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog)
import requests
from bs4 import BeautifulSoup
import os


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Web Scraper")
        self.setGeometry(100, 100, 800, 600)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Enter URL")
        self.search_box.returnPressed.connect(self.scrape)

        self.results = QTextEdit(self)
        self.results.setReadOnly(True)

        self.scrape_button = QPushButton("Scrape", self)
        self.scrape_button.clicked.connect(self.scrape)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_file)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter URL: "), alignment=Qt.AlignLeft)
        layout.addWidget(self.search_box)
        layout.addWidget(QLabel("Results: "), alignment=Qt.AlignLeft)
        layout.addWidget(self.results)
        layout.addStretch()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.scrape_button)
        button_layout.addWidget(self.save_button)
        layout.addLayout(button_layout)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def scrape(self):
        url = self.search_box.text()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        result_text = soup.get_text()

        self.results.setPlainText(result_text)

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as f:
                f.write(self.results.toPlainText())
            os.startfile(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())