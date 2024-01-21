#підключення бібліотек
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QMessageBox,QRadioButton,QComboBox
from random import randint
app=QApplication([])
# Зберігання посилання на вікно "Транспорт"
transport_win = None
show_avto = None
#створення дод вікон
def show_paris():
    victory_win=QMessageBox()
    victory_win.setText('Австрія')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_london():
    victory_win=QMessageBox()
    victory_win.setText('Польща - Тут була прийнята перша Європейська Конституція')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_german():
    victory_win=QMessageBox()
    victory_win.setText('Угорщина')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_itali():
    victory_win=QMessageBox()
    victory_win.setText('Молдова')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_amer():
    victory_win=QMessageBox()
    victory_win.setText('Північна Корея')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_litak():
    victory_win=QMessageBox()
    victory_win.setText('Вірно ти виграв!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_korabel():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_poizd():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_car():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_info(message):
    info_win = QMessageBox()
    info_win.setText(message)
    info_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    info_win.setWindowTitle('Інформація')
    info_win.exec_()
#Створення другого вікна (2 вікно)   
def show_transport_window():
    global transport_win
    transport_win = QWidget()
    transport_win.setWindowTitle('Транспорт')
    transport_win.resize(530, 530)
    transport_win.setStyleSheet("background-color: red; font-size: 16px; font-weight: bold;")

    question = QLabel('Виберіть транспортні засоби на яких ви будете подорожувати:')
    #Додати машини
    combo_transport1 = QComboBox()
    combo_transport1.addItem('Nissan')
    combo_transport1.addItem('Jaguar')
    combo_transport1.addItem('Volvo')
    combo_transport1.addItem('Ferrari')
    combo_transport1.addItem('Porsche')
    # Додати літаки
    
    combo_transport2 = QComboBox()
    combo_transport2.addItem('Мрія')
    combo_transport2.addItem('Boeing 737')
    combo_transport2.addItem('Dassault Falcon 2000')
    combo_transport2.addItem('McDonnell Douglas DC-9')
    combo_transport2.addItem('Lockheed Martin X-59 QueSST')
    # Додати поїзда
    
    combo_transport3 = QComboBox()
    combo_transport3.addItem('Швидкісний купе ')
    combo_transport3.addItem('Швидкісний плацкарт')
    combo_transport3.addItem('Звичайний купе')
    combo_transport3.addItem('Звичайний плацкарт')
    # Додати кораблі
    
    combo_transport4 = QComboBox()
    combo_transport4.addItem('Club Med 2')
    combo_transport4.addItem('Wind Surf')
    combo_transport4.addItem('S/Y A')
    combo_transport4.addItem('Royal Clipper')
    # Додайте інші можливості вибору, які потрібні
    
    btn_choose_items = QPushButton('Вибрати транспорт')
    btn_styles = "font-size: 16px; font-weight: bold;"
    question.setStyleSheet(btn_styles)
    combo_transport1.setStyleSheet(btn_styles)
    combo_transport2.setStyleSheet(btn_styles)
    combo_transport3.setStyleSheet(btn_styles)
    combo_transport4.setStyleSheet(btn_styles)
    btn_choose_items.setStyleSheet(btn_styles)
    
    layout_main = QVBoxLayout()
    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutH3 = QHBoxLayout()
    layoutH4 = QHBoxLayout()
    layoutH5 = QHBoxLayout()

    layoutH1.addWidget(question, alignment=Qt.AlignCenter)
    layoutH2.addWidget(QLabel('Машини:'))
    layoutH2.addWidget(combo_transport1)
    layoutH3.addWidget(QLabel('Літаки:'))
    layoutH3.addWidget(combo_transport2)
    layoutH4.addWidget(QLabel('Поїзда:'))
    layoutH4.addWidget(combo_transport3)
    layoutH5.addWidget(QLabel('Кораблі:'))
    layoutH5.addWidget(combo_transport4)
    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)
    layout_main.addLayout(layoutH3)
    layout_main.addLayout(layoutH4)
    layout_main.addLayout(layoutH5)
    layout_main.addWidget(btn_choose_items, alignment=Qt.AlignCenter)
    transport_win.setLayout(layout_main)

    btn_choose_items.clicked.connect(show_new_window)
    transport_win.show()
#Третє вікно
def show_new_window():
    global new_win
    new_win = QWidget()
    new_win.setWindowTitle('Необхідне')
    new_win.resize(550, 530)
    new_win.setStyleSheet("background-color: orange; font-size: 16px; font-weight: bold;")

    question = QLabel('Речі які вам потрібно в подорожі')
    combo_items = QComboBox()
    combo_items.setEditable(True)  # Дозволяє вводити речі вручну
    btn_plus = QPushButton("Додати")
    btn_choice1 = QPushButton('Вийти')

    btn_styles = "font-size: 16px; font-weight: bold;"
    question.setStyleSheet(btn_styles)
    combo_items.setStyleSheet(btn_styles)
    btn_choice1.setStyleSheet(btn_styles)

    layout_main = QVBoxLayout()
    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutH3 = QHBoxLayout()

    layoutH1.addWidget(question, alignment=Qt.AlignCenter)
    layoutH2.addWidget(QLabel('Введіть речі, які ви хочете взяти:'))
    layoutH2.addWidget(combo_items)
    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)
    layout_main.addLayout(layoutH3)
    layout_main.addWidget(btn_choice1, alignment=Qt.AlignCenter)
    layoutH3.addWidget (btn_plus, alignment=Qt.AlignCenter)

    new_win.setLayout(layout_main)

    def exit_window():
        QCoreApplication.quit()
    def add_item():
        text = combo_items.currentText()
        combo_items.addItem(text)
        combo_items.setCurrentText("")  # Очищає поле після додавання

    btn_choice1.clicked.connect(exit_window)
    btn_plus.clicked.connect(add_item)
    new_win.show()
#Створення головного (1вікна)
main_win=QWidget()
main_win.setWindowTitle('Подорожі')
main_win.resize(530,530)
#Колір фону та розмір тексту
main_win.setStyleSheet("background-color: lightgreen; font-size: 16px; font-weight: bold;")
#створення віджетів головного вікна
question=QLabel('В яку країну ви хочете поїхати?')
btn_answer1=QRadioButton('Польща')
btn_answer2=QRadioButton('Австрія')
btn_answer3=QRadioButton('Угорщина')
btn_answer4=QRadioButton('Молдова')
btn_answer5=QRadioButton('Північна Корея')
btn_next=QPushButton('На чому їдемо?')#Кнопка по середині
# Застосування стилів до кнопок(шрифт)
text_styles = "font-size: 16px; font-weight: bold;"
btn_answer1.setStyleSheet(text_styles)
btn_answer2.setStyleSheet(text_styles)
btn_answer3.setStyleSheet(text_styles)
btn_answer4.setStyleSheet(text_styles)
btn_answer5.setStyleSheet(text_styles)

btn_next.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #c1ccde;")
#розташування віджетів по лейаутам
layout_main= QVBoxLayout()
layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()
layoutH4=QHBoxLayout()
layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_next,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer3,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer4,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer5,alignment=Qt.AlignCenter)


layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
main_win.setLayout(layout_main)
#обробка натискань на перемикачі
btn_answer1.clicked.connect(show_london)
btn_answer2.clicked.connect(show_paris)
btn_answer3.clicked.connect(show_german)
btn_answer4.clicked.connect(show_itali)
btn_answer5.clicked.connect(show_amer)
btn_next.clicked.connect(show_transport_window)


#відображення вікна додатка 
main_win.show()
app.exec_()