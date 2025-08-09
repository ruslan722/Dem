'''тест для создания графического интерфейса с помощью tkinter'''
import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk

root = tk.Tk() #Создание корневого окна
root.title('Учет материалов') #Заголовок окна
root.geometry('800x400') #Размеры окна
root.resizable(False, False) #Запрет изменения размеров окна
root.configure(bg="#040101") #Установка цвета фона окна

header = Label(root, text='Cклад материалов', font=('Arial', 28), bg='white', fg='black' , width=40)
header.place(x=0, y=10) #Размещение заголовка в окне
button = Button(root, text='Показать материалы',
                 font=('Gabriola', 16), bg='#2D6033', fg='white', width=30)
button.place(x=280, y=80) #Размещение кнопки в окне


root.mainloop() #Запуск главного цикла обработки событий
