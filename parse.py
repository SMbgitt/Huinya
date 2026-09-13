import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def selectById(id):
    user = cursor.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
    return user

def selectAll():
    rows = cursor.execute('SELECT * FROM users').fetchall()
    return rows

def selectByName(name):
    rows = cursor.execute('SELECT * FROM users WHERE fio LIKE ?', ('%' + name + '%',)).fetchall()
    return rows

def selectByPhone(phone):
    rows = cursor.execute('SELECT * FROM users WHERE phone LIKE ?', ('%' + phone + '%',)).fetchall()
    return rows

def selectFree(request):
    rows = cursor.execute(request).fetchall()
    return rows

def insert(fio = "", phone = "", descr = "", address = ""):
    cursor.execute('INSERT INTO users (fio,phone,descr,address) VALUES (?, ?, ?, ?)', (fio, phone, descr, address))
    conn.commit()

def update(id = 0, fio = "", phone = "", descr = "", address = ""):
    cursor.execute('UPDATE users SET fio = ?, phone = ?, descr = ?, address= ? WHERE id = ?', (fio, phone, descr, address, id))
    conn.commit()

def delete(id):
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()

def deleteALLUSERS():
    cursor.execute('DELETE FROM users')
    conn.commit()