f = open('book.txt', 'a')
f.close()

from read import read_book 
from add import add_contact
from search import search_contact
from delete import delete_contact
from copy_contact import copy_contact
from copy_is_file import copy_cont_file
from change import change
  
def check(n):
    while not n.isdigit():
        n = input('Введите пункт цифрой: ')
    n = int(n)   
     
    while not 1 <= n <= 8:
        n = int(input('Такой пункт отсутствует, введите корректную цифру: '))
    
    return int(n)


def menu():   
    value = None
    while value != 8:
        value = input('Выберите пункт, что необходимо сделать:\n'
        '1. Посмотреть телефонную книгу\n'
        '2. Поиск контакта\n'
        '3. Добавить контакт\n'
        '4. Удалить контакт\n'
        '5. Копирование контакта в новый файл\n'
        '6. Копирование контакта из другого файла\n'
        '7. Изменить контакт\n'
        '8. Выйти из телефонной книги\n'
        'для выбора введите далее цифру: ')
        value = check(value)
       
        if int(value) == 1:
            read_book()

        elif int(value) == 3:
            add_contact()

        elif int(value) == 2:
            search_contact()

        elif int(value) == 4:
            delete_contact()

        elif int(value) == 5:
            copy_contact()

        elif int(value) == 6:
            copy_cont_file()

        elif int(value) == 7:
            change()
menu()