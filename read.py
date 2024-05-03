def read_book():
    with open('book.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        if data == []:
            print()
            print('Телефонная книга пуста, вы можете добавить контакт, для этого в главном меню нажмите цифру 3\n')
        else:
            
            [print(i+1, data[i].ljust(20)) for i in range(len(data))]