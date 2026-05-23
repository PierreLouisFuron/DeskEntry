
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class ConfirmDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")

        QBtn = (QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Are you sure ?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)