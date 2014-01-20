import mysql.connector
from datetime import date, datetime, timedelta
cn = mysql.connector.connect(user='root', database='emp',password='root',host='127.0.0.1') #creating connection
cr = cn.cursor() #handle structure (like dataatapter)
tomorrow = datetime.now().date() + timedelta(days=1)
query="INSERT INTO employees(first_name, last_name, hire_date, gender, birth_date) VALUES('{}','{}','{}','{}','{}')".format("Arun","Kumar",tomorrow,'M',date(1988,9,24))
cr.execute(query)
emp_no = cr.lastrowid
print("We Inserted the Employee Number of {0} ".format(emp_no))
cr.commit()
cr.close() #closing the cursor
cn.close() #closing the connection

