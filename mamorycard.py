from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import( 
    QApplication, QWidget, QTableWidget, QListWidget, 
     QLineEdit, QFormLoyout, QHBoxLayout, 
      QVBoxLayout, QGroupBox, QButtonGroup, 
      QPushButton, QLabel, QRadioButton, QSpinBox) 
app= QApplication([])
from marian import *


list_question =QlistView()
widget_ans=QWidget()
widget_ans.setLayout(layout_form)
btn_add=QPushButton("нове запитання")
btn_del=QPushButton("вилучити")
btn_start=QPushButton("початок тесту")
qst_col=QVBoxLayout()#Question collone(стовпчик з питаннями)
qst_col.addWidget(list_question)
qst_col.addWidget(btn_add)

ans_col=QVBoxLayout()
ans_col.addWidget(widget_ans)
ans_col.addWidget(btn_del)


btn_line=QHBoxLayout()
btn_line.addLayout(qst_col)
btn_line.addLayout(ans_col)

test_line=QHBoxLayout()
test_line.addStretch(1)
test_line.addWidget(btn_start, stretch=2)
layout_screen=QVBoxLayout()
layout_screen.addLayout(btn_line)
layout_screen.addLayout(test_line)

