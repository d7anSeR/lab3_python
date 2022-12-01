import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QMessageBox, QPushButton, QVBoxLayout, QTabWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont


from task1 import create_csv1
from task2 import copy_dir2
from task3 import copy_dir3
from task5 import Iterator1
import codecs


class Example(QWidget):

    def __init__(self) -> None:
        '''class constructor'''
        super().__init__()
        self.__iterator1 = Iterator1("dataset", "good")
        self.__iterator2 = Iterator1("dataset", "bad")
        self.__lable = QLabel(self)
        self.__path = ""
        self.initUI()

    def initUI(self) -> None:
        '''the method that sets the main parameters of the window'''
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Laboratory Work №2 on application programming')
        self.setWindowIcon(QIcon('icon.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.__tasks(), "tasks")
        tabs.addTab(self.__show_review(), "show review")
        self.__iterator1.path = self.__path
        self.__iterator2.path = self.__path
        layout.addWidget(tabs)
        self.show()

    def __good(self) -> None:
        '''the method of displaying a good review on the screen'''
        if 'dataset' not in self.__path:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("don't choose the folder")
            error.exec_()
            return
        try:
            self.__iterator1.path = "good"
            new = os.path.join(os.path.join(
                self.__iterator1.folder, self.__iterator1.path), self.__iterator1.__next__())
            print(new)
            f = codecs.open(new, 'r', 'utf-8')
            self.__review = f.read()
            self.__lable.setText(self.__review)
            f.close()
        except:
            print("error when tried to open file")

    def __bad(self) -> None:
        '''the method of displaying a bad review on the screen'''
        if 'dataset' not in self.__path:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("don't choose the folder")
            error.exec_()
            return
        try:
            self.__iterator2.path = "bad"
            new = os.path.join(os.path.join(
                self.__iterator2.folder, self.__iterator2.path), self.__iterator2.__next__())
            print(new)
            f = codecs.open(new, 'r', 'utf-8')
            self.__review = f.read()
            self.__lable.setText(self.__review)
            f.close()
        except:
            print("error when tried to open file")

    def __tasks(self) -> QWidget:
        '''method for working with dataset by tasks'''
        tasks_tab = QWidget()
        layout = QHBoxLayout()
        self.__button = QPushButton("Select a directory", self)
        self.__button.clicked.connect(self.insert_dir)
        layout.addWidget(self.__button)
        task1 = QPushButton('task1')
        task1.clicked.connect(self.__task1)
        layout.addWidget(task1)
        task2 = QPushButton('task2')
        task2.clicked.connect(self.__task2)
        layout.addWidget(task2)
        task3 = QPushButton('task3')
        task3.clicked.connect(self.__task3)
        layout.addWidget(task3)
        layout.addSpacing(100)
        tasks_tab.setLayout(layout)
        return tasks_tab

    def __show_review(self) -> QWidget:
        '''method for implementing the transition to the following instances of classes'''
        show_review = QWidget()
        layout = QHBoxLayout()
        layout_button = QVBoxLayout()
        next_good = QPushButton("next_good")
        next_good.clicked.connect(self.__good)
        layout_button.addWidget(next_good)
        next_bad = QPushButton("next_bad")
        next_bad.clicked.connect(self.__bad)
        layout_button.addWidget(next_bad)
        self.__lable.setFont(QFont("Times", 7))
        self.__lable.setGeometry(QtCore.QRect(0, 1000, 1000, 50))
        self.__lable.setWordWrap(True)
        self.__lable.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignLeft)
        layout.addWidget(self.__lable)
        layout.addLayout(layout_button)
        show_review.setLayout(layout)
        return show_review

    def __task1(self) -> None:
        '''method for working on task1'''
        if 'dataset' not in self.__path:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("don't choose the folder")
            error.exec_()
            return
        print("task1")
        create_csv1("good", "bad", QFileDialog.getExistingDirectory(
            self, 'Select Folder'), "annotation1")

    def __task2(self) -> None:
        '''method for working on task2'''
        if 'dataset' not in self.__path:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("don't choose the folder")
            error.exec_()
            return
        print("task2")
        copy_dir2("good", "bad", QFileDialog.getExistingDirectory(
            self, 'Select Folder'), "annotation2")

    def __task3(self) -> None:
        '''method for working on task3'''
        if 'dataset' not in self.__path:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("don't choose the folder")
            error.exec_()
            return
        print("task3")
        copy_dir3("good", "bad", QFileDialog.getExistingDirectory(
            self, 'Select Folder'), "annotation3")

    def insert_dir(self) -> None:
        '''method for selecting the main folder'''
        flag = True
        while flag:
            self.__folderpath = QFileDialog.getExistingDirectory(self)
            if "dataset" not in self.__folderpath:
                error = QMessageBox()
                error.setWindowTitle("Error")
                error.setText("error when selecting a folder")
                error.exec_()
            else:
                flag = False
                self.__path = "dataset"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    