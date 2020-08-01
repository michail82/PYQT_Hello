from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction,QMenu
from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot


class MainWindow( QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        action_test_title = QCoreApplication.translate("MainWindow",'Test action')
        self.__action_test = QAction(parent=self)
        self.__action_test.setText(action_test_title)

        action_quit_title = QCoreApplication.translate("MainWindow", 'Quit')
        self.__action_quit = QAction(parent=self)
        self.__action_quit.setText(action_quit_title)
        self.__action_quit.triggered.connect(self.close())


        action_manual_title = QCoreApplication.translate("MainWindow", 'User manual')
        self.__action_manual = QAction(parent=self)
        self.__action_manual.setText(action_manual_title)

        action_aboutqt_title = QCoreApplication.translate("MainWindow", 'About QT...')
        self.__action_aboutqt = QAction(parent=self)
        self.__action_aboutqt.setText(action_aboutqt_title)
        self.__action_aboutqt.triggered.connect(self.on_about_qt)

        action_about_title = QCoreApplication.translate("MainWindow", 'About ...')
        self.__action_about = QAction(parent=self)
        self.__action_about.setText(action_about_title)
        self.__action_about.triggered.connect(self.on_about)

#Menu
        menu_file_title = QCoreApplication.translate('MainMenu', 'File')
        menu_file = QMenu(parent=self)
        menu_file.setTitle(menu_file_title)
        menu_file.addAction(self.__action_test)
        menu_file.addSeparator()
        menu_file.addAction(self.__action_quit)
        self.menuBar().addMenu(menu_file)

        menu_help_title = QCoreApplication.translate('MainMenu', 'Help')
        menu_help = QMenu(parent=self)
        menu_help.setTitle(menu_help_title)
        menu_help.addAction(self.__action_manual)
        menu_help.addSeparator()
        menu_help.addAction(self.__action_aboutqt)
        menu_help.addAction(self.__action_about)
        self.menuBar().addMenu(menu_help)
@pyqtSlot()
def on_about_qt (self):
     QMessageBox.aboutQt(parent=self)

def on_about(self):
    title = QCoreApplication.translate('MainWindow','About')
    text = QCoreApplication.translate(
        'MainWindow',
        'This is our beutiful "Hollo world!"program'

    )
    QMessageBox.about(self,title,text)