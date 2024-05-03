from read import read_book

def change():
    with open('book.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        
        
    if data != []:
        read_book()
        var = int(input('Введите порядковый номер контакта, который хотите изменить: '))
        while not 0 <= var-1 <= len(data)-1: 
            var = int(input('Такого контакта не существует, введите корректный номер: '))
            

            
        s = input('Введите фамилию: ') + ' '
        n = input("Введите имя: ") + ' '
        p = input('Введите отчество: ') + ' '
        num = input('Введите номер телефона: ') + '\n'
        data_contakt = [s.lower().title(), n.lower().title(), p.lower().title(), num]
        data[var-1] = ''.join(data_contakt)

        print(data)
        with open('book.txt', 'w+', encoding='utf-8') as file:
            for item in data:
                file.write(item)