def search_contact():
    
    data_search = input('Введите данные, по которым хотите начать поиск: ').split()
    print()
    
    with open('book.txt', 'r', encoding='utf-8') as f:
        book = f.readlines()
        if book != []:
            message = 'Такого контакта не найдено'
            mess = []
            n = None
            for li in book:
                for el in data_search:
                    n = li.lower().find(el.lower())
                    if n == -1:
                        break
                if not n == -1:
                    mess.append(li)
                # if data_search.lower() in li.lower():
                #     mess.append(li)
            if mess == []:
                print(message)
            else:
                [print(el) for el in mess]    
            print()
        else:
            print('Телефонная книга пуста')
            print()