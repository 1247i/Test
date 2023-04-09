from PyQt5.QtCore import Qt
#создай приложение для запоминания информацииfrom PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup  ,  QGroupBox, QMessageBox,QHBoxLayout,QApplication,QWidget,QRadioButton, QPushButton, QLabel,QVBoxLayout
from random import shuffle,randint
class Question():
    def __init__(self,question,right_answ,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answ=right_answ
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

questions=list()
questions.append(Question('2+2','4','1990','0','1'))
questions.append(Question('8/0','нельзя','19821','8','0'))
questions.append(Question('В каком году вышел Metal Gear Solid 2  на PS2','2001','1999','2005','2004'))
questions.append(Question('Кто является главным героем MGS 3','Биг Босс','Солид Снейк','Райден','Сенатор Армстронг'))
app=QApplication([])
main_win=QWidget()
main_win.show()
main_win.setWindowTitle('Тест')
btn_OK= QPushButton('Ответить')
lb_question=QLabel('вопросы')
RadioGroupBox=QGroupBox('Варианты ответов')
rbutton_a1=QRadioButton('Вариант1')
rbutton_a2=QRadioButton('вариант 2')
rbutton_a3=QRadioButton('Вариант 3')
rbutton_a4=QRadioButton('Вариант 4')
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbutton_a1)
RadioGroup.addButton(rbutton_a2)
RadioGroup.addButton(rbutton_a3)
RadioGroup.addButton(rbutton_a4) 
layout_ans1=QHBoxLayout()
layout_ans2=QHBoxLayout()
layout_ans3=QHBoxLayout()
layout_ans2.addWidget(rbutton_a1)
layout_ans2.addWidget(rbutton_a2)
layout_ans3.addWidget(rbutton_a3)
layout_ans3.addWidget(rbutton_a4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line1.addWidget(lb_question,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)
layout_card= QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(8)
AnsGroupBox =QGroupBox('Результат теста')
ib_Result =QLabel('прав ты или нет')
ib_Correct=QLabel('Ответ будет тут')
layout_res=QHBoxLayout()
layout_res.addWidget(ib_Result,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_res.addWidget(ib_Correct,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
AnsGroupBox.setLayout(layout_res)
ib_qustion=QLabel('Самый сложный вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbutton_a2.setChecked(False)
    rbutton_a1.setChecked(False)
    rbutton_a3.setChecked(False)
    rbutton_a4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
answers=[rbutton_a1,rbutton_a2,rbutton_a3,rbutton_a4]
def ask(q :Question):
    shuffle(answers)
    answers[0].setText(q.wrong1)
    answers[1].setText(q.wrong2)
    answers[2].setText(q.right_answ)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    ib_Correct.setText(q.right_answ)
    show_question()
def next_question():
    main_win.total +=1
    
    i=randint(0,len(questions)-1)
    ask(questions[i])

def show_correct(res):
    ib_Result.setText(res)  
    show_result() 
def check_answ():
    if answers[2].isChecked():
        main_win.right +=1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[0].isChecked() or answers[3].isChecked ():
            show_correct('Нет!')
    print('Статистика:')
    print('Всего вопросов:',main_win.total,'\nПравильных ответов',main_win.right)
    print('Рейтинг:',int(main_win.right*100/main_win.total),'%')
def click_OK():
    if btn_OK.text()=='Ответить':
        check_answ()
    else:
        next_question()

main_win=QWidget()
main_win.n_question=-1 
main_win.total=0
main_win.right=0
next_question()

main_win.setLayout(layout_card)
main_win.show() 
main_win.setWindowTitle('Тест')
btn_OK.clicked.connect(click_OK)        
app.exec_()   
