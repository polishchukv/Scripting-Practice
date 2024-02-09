import sys
import requests
import json
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # API endpoint
        self.url = "https://qualysapi.qualys.com/api/2.0/fo/report/"

        # API credentials
        self.api_username = "your_username"
        self.api_password = "your_password"

        # Create the central widget
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create the layout
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Create the list widget
        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)

        # Populate the list widget with available reports
        self.populate_list()

        # Connect the list widget to the download function
        self.list_widget.itemDoubleClicked.connect(self.download_report)

    def populate_list(self):
        # Make a request to the API to get a list of available reports
        response = requests.get(self.url, auth=(self.api_username, self.api_password))

        # Check if the request was successful
        if response.status_code == 200:
            # Load the response into a dictionary
            data = json.loads(response.text)

            # Add the available reports to the list widget
            for report in data['RESPONSE']['RESULT']['REPORT']:
                item = QtWidgets.QListWidgetItem(report['TITLE'])
                self.list_widget.addItem(item)
        else:
            # If the request was not successful, show an error message
            error_message = QtWidgets.QMessageBox.critical(
                self, "Error", "Failed to retrieve reports: {}".format(response.text))

    def download_report(self, item):
        # Get the selected report title
        report_title = item.text()

        # Make a request to download the selected report
        response = requests.get(self.url + report_title, auth=(self.api_username, self.api_password))

        # Check if the request was successful
        if response.status_code == 200:
            # Save the report to a file in the current directory
            with open("report.pdf", "wb") as f:
                f.write(response.content)
            # Show a success message
            success_message = QtWidgets.QMessageBox.information(
                self, "Success", "Report saved to report.pdf")
        else:
            # If the request was not successful, show an error message
            error_message = QtWidgets.QMessageBox.critical(
                self, "Error", "Failed to download report: {}".format(response.text))
# Create the application and main window
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

# Run the application
sys.exit(app.exec_())
