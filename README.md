# 📌 PyQt6 기반 GUI 애플리케이션 구성 설명

## 🧩 프로그램 개요

이 애플리케이션은 PyQt6을 기반으로 GUI를 구성하며, 여러 기능이 **클래스 단위**로 모듈화되어 관리됩니다.  
메인 윈도우 (`app.py`)에서 서브 기능 창 (`pyQTapp04.py`)을 실행할 수 있으며, 코드 재사용성과 유지보수성을 고려해 각 기능을 독립된 클래스로 구성하였습니다.

---

## 📁 프로젝트 구성 파일

├── res/
│ ├── mainWindow.ui # 메인 윈도우 UI
│ └── fbDialog.ui # 서브 기능창 (Mini Facebook UI)
├── add.txt # 텍스트 저장 파일
├── pyQTapp01.py # 기본 UI 로딩 예제
├── pyQTapp02.py # 기능 확장 버전 (미제공)
├── pyQTapp03.py # 기능 확장 버전 (미제공)
├── pyQTapp04.py # 기능창 (Mini Facebook) - 클래스 버전
└── app.py # 메인 실행 파일

---

## 💻 주요 클래스 및 역할

### 1. `pyQTapp01.py`  
> **UI를 불러오는 가장 기본적인 예제**

```python
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
```
클래스 없이 단순히 UI를 불러오고 표시만 함

### 2. `pyQTapp04.py` → `myWindow` 클래스  
> **Mini Facebook 기능창 구성 클래스**

```python
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QApplication
from PyQt6 import uic
import csv

Form, Window = uic.loadUiType("res/fbDialog.ui")

class myWindow:
    def __init__(self):
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

        # 버튼과 함수 연결
        self.form.btnSubmit.clicked.connect(self.save_to_csv)
        self.form.btnSearch.clicked.connect(self.fine_from_csv)
        self.form.btnAddPhoto.clicked.connect(self.add_photo)

    def save_to_csv(self):
        text1 = self.form.lineEdit.text() if self.form.lineEdit.text() else ""
        text2 = self.form.lineEdit_2.text() if self.form.lineEdit_2.text() else ""
        text3 = self.form.lineEdit_3.text() if self.form.lineEdit_3.text() else ""
        with open("add.txt", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([text1, text2, text3])

    def fine_from_csv(self):
        self.form.lineEdit.clear()
        self.form.lineEdit_2.clear()
        self.form.lineEdit_3.clear()
        with open("add.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    self.form.lineEdit.setText(row[0])
                    self.form.lineEdit_2.setText(row[1])
                    self.form.lineEdit_3.setText(row[2])
                    break

    def add_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            pixmap = QPixmap(file_path)
            self.form.lblPhoto.setPixmap(pixmap)
            self.form.lblPhoto.setScaledContents(True)
            self.form.lineEdit_3.setText(file_path)

    def lounch(self):
        self.window.show()

if __name__ == "__main__":
    app = QApplication([])
    mw = myWindow()
    mw.window.show()
    app.exec()
```

 #### 📌 주요 기능 설명

| 함수 이름         | 기능 설명                                             |
|------------------|-------------------------------------------------------|
| `__init__()`     | UI 초기화 및 버튼 이벤트 연결                           |
| `save_to_csv()`  | 입력된 텍스트 데이터를 `add.txt` 파일에 저장             |
| `fine_from_csv()`| 파일에서 첫 번째 데이터 행을 읽어와 입력칸에 표시         |
| `add_photo()`    | 이미지 파일 선택 후, 화면에 표시 및 경로 저장            |
| `lounch()`       | 윈도우 창을 화면에 표시                                |
