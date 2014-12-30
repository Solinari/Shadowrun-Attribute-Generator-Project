# put some queries here
# or other stuff
import sqlite3

# make database, point cursor, access table
con = sqlite3.connect('Attributes.db')

cur = con.cursor()

##cur.execute('SELECT * FROM AttributeData WHERE Agility > 4')
##print(cur.fetchall())
