'''
Created on Apr 25, 2010

@author: Lamneth
'''

import sqlite3

def CreateAccountDatabase():
    con = sqlite3.connect('Accounts.database')
    con.isolation_level = None
    cur = con.cursor()
    
    cur.execute('''create table accounts(name text, password text)''')
    
    cur.execute("""insert into accounts values ('lamneth','testpass')""")
    
    con.commit()
    
    con.close()
    
def FindAccount(name, password):
    con = sqlite3.connect('Accounts.database')
    con.isolation_level = None
    cur = con.cursor()
    nameC = (name,)
    cur.execute('select password from accounts where name=?', nameC)
    con.commit()
    con.close()
    return password == cur.fetchone()[0]
    
    
#CreateAccountDatabase()
FindAccount('lamneth', 'testpass')