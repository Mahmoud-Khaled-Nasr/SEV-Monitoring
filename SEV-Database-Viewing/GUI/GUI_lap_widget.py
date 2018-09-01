from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont


class LapWidget(QWidget):
    def __init__(self, lap_name: str, lap_id: int):
        super(LapWidget, self).__init__()
        self.lap_id = lap_id
        # Create the list item widget and its children
        lap_name_label = QLabel(lap_name)
        # Create and set the font
        widget_font = QFont()
        widget_font.setFamily("Bahnschrift SemiBold SemiConden")
        widget_font.setPointSize(16)
        lap_name_label.setFont(widget_font)
        # select_button.setFont(widget_font)
        # Set the layout
        layout = QHBoxLayout()
        layout.addWidget(lap_name_label)
        # layout.addWidget(select_button)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(20)
        self.setLayout(layout)