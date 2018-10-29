from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont


class LapWidget(QWidget):
    def __init__(self, lap_name: str, lap_id: int, lap_start_datetime):
        super(LapWidget, self).__init__()
        self.lap_id = lap_id
        self.lap_start_datetime = lap_start_datetime
        # Create the list item widget and its children
        lap_name_label = QLabel(lap_name)
        lap_start_datetime_label = QLabel(lap_start_datetime)
        # Create and set the font
        widget_font = QFont()
        widget_font.setFamily("Century Gothic")
        widget_font.setPointSize(16)
        lap_name_label.setFont(widget_font)
        lap_start_datetime_label.setFont(widget_font)
        # select_button.setFont(widget_font)
        # Set the layout
        layout = QHBoxLayout()
        layout.addWidget(lap_name_label)
        layout.addWidget(lap_start_datetime_label)
        # layout.addWidget(select_button)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(20)
        self.setLayout(layout)