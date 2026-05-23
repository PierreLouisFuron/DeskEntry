

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtUiTools import QUiLoader

from models.desktopIconFile import DesktopIconFile

FORM_UI = './views/dif_editor.ui'

class DesktopIconFileEditor(QWidget):
    
    def __init__(self, parent=None, dif=None):
        super(DesktopIconFileEditor, self).__init__(parent)
        self.parent_widget = parent

        self.load_ui()

        boolean_fields = ['', 'True', 'False']
        self.widget.cb_type.addItems(['Application', 'Link', 'Directory'])
        self.widget.cb_terminal.addItems(boolean_fields)
        self.widget.cb_no_display.addItems(boolean_fields)
        self.widget.cb_dbus_activatable.addItems(boolean_fields)
        self.widget.cb_startup_notify.addItems(boolean_fields)
        self.widget.cb_prefers_non_default_gpu.addItems(boolean_fields)
        self.widget.cb_single_main_window.addItems(boolean_fields)
        self.widget.cb_hidden.addItems(boolean_fields)

        self.widget.btn_ok.clicked.connect(self.on_btn_ok_clicked)
        self.widget.btn_cancel.clicked.connect(self.on_btn_cancel_clicked)

        if dif is not None:
            self.widget.le_name.setText(dif.name)
            # self.widget.cb_type.setText(dif.type)
            self.widget.le_exec.setText(dif.exec)
            # self.widget.cb_terminal.setText('' if dif.terminal == '' else 'true' if dif.terminal else 'false')
            self.widget.le_icon.setText(dif.icon)
            self.widget.le_comment.setText(dif.comment)
            self.widget.le_categories.setText(str(dif.categories))
            self.widget.le_version.setText(str(dif.version))
            self.widget.le_path.setText(dif.path)

        self.widget.cb_type.currentIndexChanged.connect(self.on_dif_type_changed)
        
    def on_dif_type_changed(self):
        type = self.widget.cb_type.currentText()
        if type == 'Application':
            self.widget.widget_try_exec.setVisible(True)
            self.widget.widget_exec.setVisible(True)
            self.widget.widget_path.setVisible(True)
            self.widget.widget_terminal.setVisible(True)
            self.widget.widget_actions.setVisible(True)
            self.widget.widget_mime_type.setVisible(True)
            self.widget.widget_categories.setVisible(True)
            self.widget.widget_keywords.setVisible(True)
            self.widget.widget_startup_notify.setVisible(True)
            self.widget.widget_startup_wm_class.setVisible(True)
            self.widget.widget_prefers_non_default_gpu.setVisible(True)
            self.widget.widget_single_main_window.setVisible(True)
            self.widget.widget_url.setVisible(False)
        elif type == 'Link':
            self.widget.widget_try_exec.setVisible(False)
            self.widget.widget_exec.setVisible(False)
            self.widget.widget_path.setVisible(False)
            self.widget.widget_terminal.setVisible(False)
            self.widget.widget_actions.setVisible(False)
            self.widget.widget_mime_type.setVisible(False)
            self.widget.widget_categories.setVisible(False)
            self.widget.widget_keywords.setVisible(False)
            self.widget.widget_startup_notify.setVisible(False)
            self.widget.widget_startup_wm_class.setVisible(False)
            self.widget.widget_prefers_non_default_gpu.setVisible(False)
            self.widget.widget_single_main_window.setVisible(False)
            self.widget.widget_url.setVisible(True)
        elif type == 'Directory':
            self.widget.widget_try_exec.setVisible(False)
            self.widget.widget_exec.setVisible(False)
            self.widget.widget_path.setVisible(False)
            self.widget.widget_terminal.setVisible(False)
            self.widget.widget_actions.setVisible(False)
            self.widget.widget_mime_type.setVisible(False)
            self.widget.widget_categories.setVisible(False)
            self.widget.widget_keywords.setVisible(False)
            self.widget.widget_startup_notify.setVisible(False)
            self.widget.widget_startup_wm_class.setVisible(False)
            self.widget.widget_prefers_non_default_gpu.setVisible(False)
            self.widget.widget_single_main_window.setVisible(False)
            self.widget.widget_url.setVisible(False)
        else:
            print('You should never get there')

    def load_ui(self):
        self.widget = QUiLoader().load(FORM_UI)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.widget)
        self.setLayout(v_layout)

    def on_btn_cancel_clicked(self):
        self.parent_widget.display_dif_explorer()

    def on_btn_ok_clicked(self):
        #TODO : VERIFY THAT THE FILENAME DOES NOT ALREADY EXIST
        #TODO : PREVENT FROM GOING FURTHER IF NAME OR TYPE ARE NOT SET OR IF SOME OTHER CONDITIONS ON THE KEYS ARE NOT MET
        dif_name = self.widget.le_name.text()
        file_name = dif_name.lower().replace(' ', '-') + '.desktop'
        dif = DesktopIconFile(
            name = dif_name,
            type = self.widget.cb_type.currentText(),
            version = self.widget.le_version.text(),
            exec = self.widget.le_exec.text(),
            file_name = file_name,
            file_path = self.parent_widget.difp.path,
            terminal = self.widget.cb_terminal.currentText(),
            icon = self.widget.le_icon.text(),
            comment = self.widget.le_comment.text(),
            categories = self.widget.le_categories.text(),
            url = self.widget.le_url.text()
        )

        self.parent_widget.difp.create_desktop_file(dif)
        dif_explorer = self.parent_widget.stack_widget.widget(0)
        dif_explorer.append_item_to_list(dif, dif_explorer.lw_desktop_files)
        self.parent_widget.display_dif_explorer()

