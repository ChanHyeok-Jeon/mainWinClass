from PyQt6.QtGui import QPixmap  # 수정: QPixmap은 PyQt6.QtGui에서 가져와야 함
from PyQt6.QtWidgets import QFileDialog
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import csv

Form, Window = uic.loadUiType("dialog.ui")

def save_to_csv():
    # Get text from line edits, default to empty string if no text
    text1 = form.lineEdit.text() if form.lineEdit.text() else ""
    text2 = form.lineEdit_2.text() if form.lineEdit_2.text() else ""
    text3 = form.lineEdit_3.text() if form.lineEdit_3.text() else ""

    # Save to add.txt in CSV format
    with open("add.txt", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([text1, text2, text3])
def fine_from_csv():
    # Clear the text in line edits before searching
    form.lineEdit.clear()
    form.lineEdit_2.clear()
    form.lineEdit_3.clear()

    # Read from add.txt and search for the first row
    with open("add.txt", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check if the row is not empty
                form.lineEdit.setText(row[0])
                form.lineEdit_2.setText(row[1])
                form.lineEdit_3.setText(row[2])
                break  # Stop after finding the first row
def add_photo():
    # Open a file dialog to select an image file
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
    )
    if file_path:  # If a file is selected
        # Set the image to lblPhoto
        pixmap = QPixmap(file_path)
        form.lblPhoto.setPixmap(pixmap)
        form.lblPhoto.setScaledContents(True)  # Scale the image to fit the label

        # Set the file path to lineEdit_3
        form.lineEdit_3.setText(file_path)


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Connect btnSubmit's clicked signal to save_to_csv function
form.btnSubmit.clicked.connect(save_to_csv)
form.btnSearch.clicked.connect(fine_from_csv)
form.btnAddPhoto.clicked.connect(add_photo)

window.show()
app.exec()
