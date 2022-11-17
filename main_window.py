import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.__button = QPushButton("Select a directory", self)
        self.__button.clicked.connect(self.insert_dir)
        self.__lable = QLabel(self)
        self.__name_dir = "new_dir"
        self.__path = "dataset"
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Laboratory Work №2 on application programming')
        self.setWindowIcon(QIcon('icon.jpg'))
        
        self.show()

    def insert_dir(self):
        flag = True
        while flag:
            folderpath = QFileDialog.getExistingDirectory(self)      
            if "dataset" not in folderpath:
                error = QMessageBox()
                error.setWindowTitle("Error")
                error.setText("error when selecting a folder")
                error.exec_()
            else:
                flag = False
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
