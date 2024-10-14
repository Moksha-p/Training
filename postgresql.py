import psycopg2

hostname = 'localhost'
database = 'MyDb'
username = 'postgres'
pwd = 'Technman2024'
port_id = '5432'
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()

    # Create table if it doesn't exist
    create_script = '''CREATE TABLE IF NOT EXISTS employee (
                          id int PRIMARY KEY,
                          name varchar(40) NOT NULL,
                          salary int,
                          dept_id varchar(30))'''
    cur.execute(create_script)

    # Check if the table exists
    cur.execute("SELECT * FROM information_schema.tables WHERE table_name='employee';")
    print("Table exists:", cur.fetchall())

    # Correct insert statement
    insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    insert_value = (2, 'djani', 112000, 'd2')  # Tuple of values
    cur.execute(insert_script, insert_value)  # Pass the tuple here

    conn.commit()

    # Check if the data was inserted
    cur.execute("SELECT * FROM employee;")
    rows = cur.fetchall()
    print("Data in table:", rows)

except Exception as error:
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
