
from PySide6.QtWidgets import QWidget, QHBoxLayout, QListWidgetItem
from PySide6.QtCore import QFile, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QIcon

DESKTOP_FILE_LIST_ITEM_UI = './views/desktop_file_list_item.ui'

class DesktopFileListItem(QWidget):

    on_btn_ok_clicked = Signal(str)
    on_item_selected = Signal(str)

    def __init__(self, dif, parent=None):
        super(DesktopFileListItem, self).__init__(parent)

        self.desktop_icon_file = dif

        self.widget = self.loadUI()

        self.widget.lb_desktop_file_name.setText(dif.name)

        pixmap = QPixmap(dif.icon)
        if pixmap.isNull():
            pixmap = QIcon.fromTheme(dif.icon).pixmap(50)
            if pixmap.isNull():
                # pixmap = QIcon.fromTheme('preferences-ubuntu-panel-symbolic').pixmap(50)
                pixmap = QIcon.fromTheme('fdsaic').pixmap(50)
        self.widget.img_desktop_file_img.setPixmap(pixmap)

    def loadUI(self):
        ui_file = QFile(DESKTOP_FILE_LIST_ITEM_UI)
        ui_file.open(QFile.ReadOnly)
        widget = QUiLoader().load(ui_file,self)
        ui_file.close()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget)
        self.setLayout(layout)

        return widget