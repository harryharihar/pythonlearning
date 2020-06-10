import psycopg2 as psy

from dbconfig import dbcon


con = psy.connect(**dbcon)
print(con)


cursor = con.cursor()
print(cursor)