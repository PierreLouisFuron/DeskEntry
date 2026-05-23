# This Python file uses the following encoding: utf-8

import os
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QListView, QListWidgetItem, QListWidget, QWidget, QVBoxLayout, QDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QFile, QSize
from PySide6.QtUiTools import QUiLoader
from faker import Faker
from numpy import append
from models.desktopIconFile import DesktopIconFile
from components.desktopFileListItem import DesktopFileListItem
from components.confirmDialog import ConfirmDialog
from pathlib import Path

DESKTOP_ICON_EDITOR_UI = './views/dif_explorer.ui'

class DesktopIconFileExplorer(QWidget):

    is_form_hidden = True

    def __init__(self, parent):
        super(DesktopIconFileExplorer, self).__init__(parent)
        self.parent_widget = parent

        self.load_ui()
        
        self.clear_labels()

        self.lw_desktop_files:QListWidget
        self.lw_desktop_files = self.widget.lw_desktop_files

        self.lw_global_desktop_files:QListWidget
        self.lw_global_desktop_files = self.widget.lw_global_desktop_files

        self.fill_list_with_items(self.lw_desktop_files, self.parent_widget.difp)
        self.fill_list_with_items(self.lw_global_desktop_files, self.parent_widget.global_difp)

        self.lw_desktop_files.currentItemChanged.connect(self.item_selected)
        # self.lw_desktop_files.itemClicked.connect(self.item_clicked)
        # self.lw_desktop_files.itemDoubleClicked.connect(self.item_double_clicked)
        self.lw_global_desktop_files.currentItemChanged.connect(self.item_selected)

        self.widget.btn_open_folder.clicked.connect(self.open_local_folder)
        self.widget.btn_open_global_folder.clicked.connect(self.on_btn_open_local_global_folder_clicked)
        self.widget.btn_new_dif.clicked.connect(self.on_btn_new_dif_clicked)
        self.widget.btn_edit_dif.clicked.connect(self.on_btn_edit_dif_clicked)
        self.widget.btn_delete_dif.clicked.connect(self.on_btn_delete_dif_clicked)

    def load_ui(self):
        self.widget = QUiLoader().load(DESKTOP_ICON_EDITOR_UI)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.widget)
        self.setLayout(v_layout)

    def get_UI(self):
        return QUiLoader().load(DESKTOP_ICON_EDITOR_UI)

    def on_btn_edit_dif_clicked(self):
        list_widget_item = self.lw_desktop_files.currentItem()
        if list_widget_item is not None: 
            dif = self.lw_desktop_files.itemWidget(list_widget_item).desktop_icon_file
            self.parent_widget.display_dif_editor(dif)

    def on_btn_new_dif_clicked(self):
        self.parent_widget.display_dif_editor()

    def on_btn_delete_dif_clicked(self):
        list_widget_item = self.lw_desktop_files.currentItem()
        if list_widget_item is not None:
            # print(dif.file_name)
            # print(dif.path)
            confirmDialog = ConfirmDialog()
            if confirmDialog.exec():
                dif = self.lw_desktop_files.itemWidget(list_widget_item).desktop_icon_file
                path = Path(f"{dif.file_path}/{dif.file_name}")
                path.unlink()
                self.lw_desktop_files.takeItem(self.lw_desktop_files.row(list_widget_item))

    def append_item_to_list(self, dif, list_widget):
        widget_item = DesktopFileListItem(dif)
        list_widget_item = QListWidgetItem()
        list_widget_item.setSizeHint(QSize(0, 40))
        list_widget.addItem(list_widget_item)
        list_widget.setItemWidget(list_widget_item, widget_item)

    def fill_list_with_items(self, list_widget, dif_parser):
        list = sorted(dif_parser.retrieve_all_desktop_icon_files(), key=lambda x: x.name)
        for dif in list:
            self.append_item_to_list(dif, list_widget)

    # def item_clicked(self):
    #     print('item clicked')

    # def item_double_clicked(self):
    #     print('item double clicked')

    def item_selected(self, selected_list_widget_item):
        widget = selected_list_widget_item.listWidget().itemWidget(selected_list_widget_item)
        dif = widget.desktop_icon_file
        self.widget.lbl_name.setText(dif.name)
        self.widget.lbl_type.setText(dif.type)
        self.widget.lbl_exec.setText(dif.exec)
        self.widget.lbl_comment.setText(dif.comment)
        self.widget.lbl_version.setText('' if dif.version == -1 else str(dif.version))
        categories = dif.categories[0] if len(dif.categories) > 0 else ''
        for category in dif.categories[1:]:
            if category != '': categories += ', ' + category
        self.widget.lbl_categories.setText(categories)
        self.widget.lbl_icon_path.setText(dif.icon)
        self.widget.lbl_terminal.setText('' if dif.terminal == '' else 'true' if dif.terminal else 'false')
        self.widget.lbl_hidden.setText('' if dif.hidden == '' else 'true' if dif.hidden else 'false')
        self.widget.lbl_generic_name.setText(dif.generic_name)
        self.widget.lbl_no_display.setText('' if dif.no_display == '' else 'true' if dif.no_display else 'false')
        self.widget.lbl_try_exec.setText(dif.try_exec)
        self.widget.lbl_path.setText(dif.path)

        actions = dif.actions[0] if len(dif.actions) > 0 else ''
        for action in dif.actions[1:]:
            if action != '': actions += ', ' + action
        self.widget.lbl_actions.setText(actions)

        self.widget.lbl_url.setText(dif.url)
        self.widget.lbl_single_main_window.setText('' if dif.single_main_window == '' else 'true' if dif.single_main_window else 'false')

        pixmap = QPixmap(dif.icon)
        if pixmap.isNull():
            pixmap = QIcon.fromTheme(dif.icon).pixmap(50)

        self.widget.lbl_icon.setPixmap(pixmap)

    def clear_labels(self):
        w = self.widget
        w.lbl_name.setText('')
        w.lbl_type.setText('')
        w.lbl_exec.setText('')
        w.lbl_comment.setText('')
        w.lbl_version.setText('')
        w.lbl_categories.setText('')
        w.lbl_icon_path.setText('')
        w.lbl_icon.setText('')
        w.lbl_terminal.setText('')
        w.lbl_hidden.setText('')
        w.lbl_generic_name.setText('')
        w.lbl_no_display.setText('')
        w.lbl_path.setText('')
        w.lbl_try_exec.setText('')
        w.lbl_actions.setText('')
        w.lbl_url.setText('')
        w.lbl_single_main_window.setText('')

    # def show(self):
    #     self.widget.show()

    def open_local_folder(self):
        self.parent_widget.difp.open_folder()

    def on_btn_open_local_global_folder_clicked(self):
        self.parent_widget.global_difp.open_folder()