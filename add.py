def add_contact():
    contakt = []
    s = input('Введите фамилию: ') + ' '
    n = input("Введите имя: ") + ' '
    p = input('Введите отчество: ') + ' '
    num = input('Введите номер телефона: ') + '\n'
    data_contakt = [s.lower().title(), n.lower().title(), p.lower().title(), num]
    
    for el in data_contakt:
        if el.lstrip() != '':
            contakt.append(el)
        

    with open('book.txt', 'a', encoding='utf-8') as f:
        for item in contakt:
            f.write(item)