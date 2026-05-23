
import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtGui import QIcon, QGuiApplication, QScreen
from components.difEditor import DesktopIconFileEditor
from components.difExplorer import DesktopIconFileExplorer
from controlers.desktopIconFileParser import DesktopIconFileParser

LOCAL_ICON_FOLDER_PATH = os.path.expanduser('~') + '/.local/share/applications'
GLOBAL_ICON_FOLDER_PATH = '/usr/share/applications'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Desktop Icon Editor')
        QIcon.setFallbackSearchPaths([
            '/usr/share/pixmaps/' ,
            '/snap/gnome-3-28-1804/161/usr/share/icons/' ,
            '/snap/gnome-3-28-1804/161/usr/share/icons/hicolor/16x16/apps'
        ])

        self.difp = DesktopIconFileParser(LOCAL_ICON_FOLDER_PATH)
        self.global_difp = DesktopIconFileParser(GLOBAL_ICON_FOLDER_PATH)

        stack_widget = QStackedWidget(self)
        stack_widget.addWidget(DesktopIconFileExplorer(self))
        self.setCentralWidget(stack_widget)
        self.stack_widget = stack_widget

    def display_dif_editor(self, dif=None):
        if self.stack_widget.count() == 2:
            self.stack_widget.removeWidget(self.stack_widget.widget(1))
        self.stack_widget.addWidget(DesktopIconFileEditor(self, dif))
        self.stack_widget.setCurrentIndex(1)

    def display_dif_explorer(self):
        self.stack_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())