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

        title = QLabel("Web Scraper")
        title.setAlignment(Qt.AlignCenter)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Enter URL")
        self.search_box.returnPressed.connect(self.scrape)
        self.search_box.setFixedHeight(50)

        self.results = QTextEdit(self)
        self.results.setReadOnly(True)
        self.results.setFixedHeight(500)
        font = self.results.font()
        font.setPointSize(20)
        self.results.setFont(font)

        self.scrape_button = QPushButton("Scrape", self)
        self.scrape_button.clicked.connect(self.scrape)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_file)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.search_box)
        layout.addWidget(self.results)
        layout.addSpacing(20)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.scrape_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        layout.addSpacing(20)

        widget = QWidget(self)
        widget.setLayout(layout)
        widget.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(widget)

    def scrape(self):
        url = self.search_box.text()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser
