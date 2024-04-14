
import json
import sqlite3 as sq

con = sq.connect("base_phon.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
            name TEXT,
            phones TEXT,
            email TEXT,
            birthday TEXT
            )""")

def serch_name(name):
    cur.execute("SELECT * FROM phonebook WHERE name = ?", name)
   
def name_del (name):
    cur.execute("DELETE FROM phonebook WHERE name = ?", name)

vihod = 1
while vihod != 0:    
    print ('1 - Поиск телефона\n2 - Просмотр телефонного справочника\n3 - Добавить новый контакт\n4 - Изменить существующий контакт\n5 - Удалить контакт\n6 - Выйти из программы')

    operation = int(input('Введите код операции - '))

    if operation == 1:
        with sq.connect("base_phon.db") as con:
            cur = con.cursor()
            a = input('Введите название контакта - ')
            serch_name (a)
            print(*cur.fetchall())

    if operation == 2:
        with sq.connect("base_phon.db") as con:
            cur.execute("SELECT * FROM phonebook;")
            res = cur.fetchall()
            for i in res:
                print (i)

    if operation == 3:
        with sq.connect("base_phon.db") as con:
            cur = con.cursor()
            a = input('Введите название контакта - ')
            b = input('Введите номер телефона - ')
            c = input('Введите email - ')
            d = input('Введите дату рождения - ')
            bs = (a, b, c, d)
            cur.execute("INSERT INTO phonebook(name, phones, email, birthday) VALUES (?, ?, ?, ?)", bs)

    if operation == 4:
        with sq.connect("base_phon.db") as con:
            name = (input('Введите название контакта - '))
            b = input('Введите номер телефона - ')
            c = input('Введите email - ')
            d = input('Введите дату рождения - ')
            cur = con.cursor()
            cur.execute("UPDATE phonebook SET  phones = ? WHERE name = ?", (b, name))
            cur.execute("UPDATE phonebook SET  email = ? WHERE name = ?", (c, name))
            cur.execute("UPDATE phonebook SET  birthday = ? WHERE name = ?", (d, name))
            print('Контакт обновлен')
        
    if operation == 5:
        name = (input('Введите имя - '))
        name_del (name)
        print('Контакт удален')

    if operation == 6:
        vihod = 0  
con.commit()
con.close()