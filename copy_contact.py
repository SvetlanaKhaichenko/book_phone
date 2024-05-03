from read import read_book

def copy_contact():
    with open('book.txt', 'r', encoding='utf-8') as f:
        book = f.readlines()

    read_book()
    if book != []:
   
        num = int(input("Введите порядковый комер контакта, который хотите скопировать: "))
        while  not 0 <= num-1 <= len(book)-1:
            num = int(input("Такой контакт отсутствует, проверьте правильность написания и введите еще раз: "))
        name_file = input('Введите название нового файла: ') + '.txt'

        contact = book[num-1]
        with open(name_file, 'a', encoding='utf-8') as file:
            file.write(contact)
        print()
        res = input(f'Хотите просмотреть содержимое {name_file}? Введите Y или нажмите ENTER для выхода в главное меню: ')
        print()
        if res.lower() == 'y':
            with open(name_file, 'r', encoding='utf-8') as f:
                data = f.readlines()
                [print(i+1, data[i].ljust(15)) for i in range(len(data))]
    