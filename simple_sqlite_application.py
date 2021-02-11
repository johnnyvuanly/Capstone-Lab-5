import sqlite3

db = 'lab_5_db.sqlite' # Created global variable just in case we need to use it often

def create_table():
    with sqlite3.connect(db) as conn: # Using context manager so we don't forget to commit
        conn.execute('CREATE TABLE IF NOT EXISTS simple (name text, country text, catches int)')
    
    conn.close()

def insert_jugglers_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO simple values ("Janne Mustonen", "Finland", "98")')
        conn.execute('INSERT INTO simple values ("Ian Stewart", "Canada", "94")')
        conn.execute('INSERT INTO simple values ("Aaron Gregg", "Canada", "88")')
        conn.execute('INSERT INTO simple values ("Chad Taylor", "USA", "78")')
    
    conn.close()

def display_all_data(): 
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM simple')
    print('All Record Holders: ')
    for row in results:
        print(row)

    conn.close()

def create_new_record_holder():
    new_name = input('Enter a new participants name: ')
    new_country = input('Which country the participant is from: ')
    new_catches = int(input('How many catches did this person have: '))

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO simple VALUES (?, ?, ?)', (new_name, new_country, new_catches))
    
    conn.close()

def display_one_record_holder(persons_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM simple WHERE name like ?', (persons_name,))
    first_row = results.fetchone()
    if first_row:
        print('Your record holder is ', first_row)
    else:
        print('Not found')
    
    conn.close()

def update_catches():
    update_name = 'Ian Stewart'
    update_catches = 105
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE simple SET name = ? WHERE catches = ?', (update_name, update_catches) )
    
    conn.close()

def delete_record_holder(persons_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from simple WHERE name = ?', (persons_name, ))
    
    conn.close()

create_table()
insert_jugglers_data()
display_all_data()
display_one_record_holder('Aaron Greg')
create_new_record_holder()
update_catches()
delete_record_holder('Chad Taylor')
print('AFTER ALL CHANGES ARE MADE')
display_all_data()