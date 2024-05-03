from read import read_book

def delete_contact():
    with open('book.txt', 'r', encoding='utf-8') as f:
        book = f.readlines()
  
    read_book()
    if book != []:
        n_delete = int(input('Введите порядковый номер контакта, который хотите удалить: '))
        while len(book) < n_delete-1 or n_delete < 0:
            n_delete = int(input('Такого контакта не существует, введите номер еще раз: '))
        
    
        
        del book[n_delete-1]
        with open('book.txt', 'w', encoding='utf-8') as f:
            for item in book:
                f.write(item)