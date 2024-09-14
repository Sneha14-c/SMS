import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='root123'
)
# step 3:check if the connections is successful

if connection.is_connected():
    print("successfully connected to the database")

    cursor=connection.cursor()
    create_table_query="""
             CREATE TABLE IF NOT EXISTS employees (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(225) NOT NULL,
                 age INT,
                 gender VARCHAR(10),
                 salary decimal(10,2),
                 bonus decimal(10,2)
                 )
                 """
    
    cursor.execute(create_table_query)
    print("table 'employees' created successfully.")
       
    insert_query="""
              INSERT INTO employees (name,age,gender,salary,bonus)
              VALUES(%s, %s, %s, %s, %s)
              """
    employees_detailes=[
                  ('Ranjitha',23,'female',90000,2000),
                  ('deepak',24,'male',80000,1500),
                  ('mithun',23,'male',85000,2000)
             ]
    cursor.executemany(insert_query,employees_detailes) 
    connection.commit()
    print(f"{cursor.rowcount} records inserted into 'employees' table")
