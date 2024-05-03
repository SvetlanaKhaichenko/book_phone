def copy_cont_file():
    name = input('Введите путь к файлу (вместе с файлом и расширением): ')
    import os.path
    path = os.path.abspath(name)
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        if data == []:
            print('Файл пуст')
        else:
            [print(i+1, data[i].ljust(15)) for i in range(len(data))]
        f.close()

    num = int(input('Введите порядковый номер контакта, который хотите скопировать в телефонную книгу: '))
    while not 0 <= num-1 <= len(data)-1:
        num = int(input('Такой контакт отсутствует, проверьте правильность написания и введите еще раз: '))
    contact = data[num-1]

    with open('book.txt', 'r', encoding='utf-8') as f:
        book = f.readlines()
    book.append(contact)
    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in book:
            f.write(item)