import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QMessageBox, QMenuBar, QMenu,QPushButton
from PyQt5.QtGui import QIcon


from task1 import run1
from task2 import create_annotation2, copy_dir2
from task3 import create_annotation3, copy_dir3

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
    
    def create_menu(self):
        self.__menuBar = QMenuBar(self)
        file_menu = QMenu("&файл", self)
        self.__menuBar.addMenu(file_menu)
        file_menu.addAction('create csv file-annotation', self.clicked)
        file_menu.addAction('copy dataset to a new directory with old numbers', self.clicked)
        file_menu.addAction('copy dataset to a new directory with new numbers', self.clicked)

    @QtCore.pyqtSlot
    def clicked(self):
        action = self.sender()
        if action.text() == 'create csv file-annotation':
            file_name = QFileDialog.getExistingDirectory(self)
            name = os.path.basename(file_name)
            run1("good", "bad", name)
        if action.text() == 'copy dataset to a new directory with old numbers':
            file_name = QFileDialog.getExistingDirectory(self)
            name = os.path.basename(file_name)
            copy_dir2(name, "good", "bad")
        if action.text() == 'copy dataset to a new directory with new numbers':
            file_name = QFileDialog.getExistingDirectory(self)
            name = os.path.basename(file_name)
            copy_dir3(name, "good", "bad")
            
            
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
