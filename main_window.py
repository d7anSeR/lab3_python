import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QMessageBox, QRadioButton, QPushButton, QVBoxLayout, QTabWidget, QHBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QIcon, QFont


from task1 import create_csv1
from task2 import create_csv2, copy_dir2
from task3 import create_csv3, copy_dir3
from task5 import Iterator1
import codecs

class Example(QWidget):

    def __init__(self):#done
        super().__init__()
        self.__button = QPushButton("Select a directory", self)
        self.__button.clicked.connect(self.insert_dir)
        self.__iterator1 = Iterator1("dataset","good")
        self.__iterator2 = Iterator1("dataset","bad")
        self.__lable = QLabel(self)
        self.__name_dir = "dataset"
        self.__path = ""
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Laboratory Work №2 on application programming')
        self.setWindowIcon(QIcon('icon.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.__general(), "general")
        tabs.addTab(self.__show_review(), "show review")
        tabs.addTab(self.__tasks(), "tasks")
        self.__iterator1.path = self.__path
        self.__iterator2.path = self.__path
        layout.addWidget(tabs)
        self.show()

    def __good(self) -> None:
        try:
            self.__iterator1.path = "good"
            new = os.path.join(os.path.join(self.__iterator1.folder, self.__iterator1.path), self.__iterator1.__next__())
            print(new)
            f = codecs.open(new, 'r', 'utf-8')
            self.__review = f.read()
            self.__lable.setText(self.__review)
            f.close()
        except:
            print("folder 'good' is over")

    def __bad(self) -> None:
        try:
            self.__iterator2.path = "bad"
            new = os.path.join(os.path.join(self.__iterator2.folder, self.__iterator2.path), self.__iterator2.__next__())
            print(new)
            f = codecs.open(new, 'r', 'utf-8')
            self.__review = f.read()
            self.__lable.setText(self.__review)
            f.close()
        except:
            print("folder 'good' is over")


    def __general(self) -> QWidget:
        general = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        menu = QLabel("Сhoose :\n 1) create CSV file for dataset\n 2) copy dataset to new directory\n 3) copy dataset with new names")
        text.addWidget(menu)
        layout.addLayout(text)
        layout.addWidget(self.__button)
        general.setLayout(layout)
        return general

    def __show_review(self) -> QWidget:
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
        self.__lable.setAlignment(QtCore.Qt.AlignJustify  | QtCore.Qt.AlignLeft)
        layout.addWidget(self.__lable)
        layout.addLayout(layout_button)
        show_review.setLayout(layout)
        return show_review

    def __tasks(self) -> QWidget:
        '''function generates tab with all buttons of prev lab'''
        tasks_tab = QWidget()
        layout = QVBoxLayout()
        task1 = QPushButton('task1')
        task1.clicked.connect(self.__task1)
        layout.addWidget(task1)
        task2 = QPushButton('task2')
        task2.clicked.connect(self.__task2)
        layout.addWidget(task2)
        task3_for_one = QPushButton('task3_for_one')
        task3_for_one.clicked.connect(self.__task3_for_one)
        layout.addWidget(task3_for_one)
        task3_for_two = QPushButton('task3_for_two')
        task3_for_two.clicked.connect(self.__task3_for_two)
        layout.addWidget(task3_for_two) 
        layout.addSpacing(100)
        layout_radio = QHBoxLayout()
        radio_button = QRadioButton("good")
        radio_button.name = "good"
        radio_button.toggled.connect(self.__click)
        layout_radio.addWidget(radio_button)
        radio_button = QRadioButton("bad")
        radio_button.name = "bad"
        radio_button.toggled.connect(self.__click)
        layout_radio.addWidget(radio_button)
        radio_button = QRadioButton("tmp")
        radio_button.name = "tmp"
        radio_button.setChecked(True)
        radio_button.toggled.connect(self.__click)
        layout_radio.addWidget(radio_button)
        layout.addLayout(layout_radio)
        tasks_tab.setLayout(layout)
        return tasks_tab
            
    def __task1(self) -> None:#done
        print("task1")
        create_csv1(self.__name, self.__path, QFileDialog.getExistingDirectory(
            self, 'Select Folder'))

    def __task2(self) -> None:#done
        print("task2!")
        copy_dir2(self.__name, self.__path, QFileDialog.getExistingDirectory(
            self, 'Select Folder'))

    def __task3_for_one(self) -> None:
        print("task3 for one")
        copy_dir3(
            self.__name, self.__path, QFileDialog.getExistingDirectory(self, 'Select Folder'))

    def __task3_for_two(self) -> None:
        print("task3 for two")
        copy_dir3(
            "good", "bad", self.__path, QFileDialog.getExistingDirectory(self, 'Select Folder'))


    def __click(self) -> None:
        '''change class name'''
        radio_button = self.sender()
        if radio_button.isChecked():
            print("Class is %s" % (radio_button.name))
            self.__iterator.setName(radio_button.name)
            self.__name = radio_button.name


    def insert_dir(self):#done
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

if __name__ == '__main__':#done

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
