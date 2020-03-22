import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                  password="Dol-fins1!",
                                  host="35.231.253.154",
                                  port="5432",
                                  database="Flask-WebAttackdata")
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE usr (ID INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL);

    CREATE TABLE post (
    ID INTEGER PRIMARY KEY,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES usr (id));'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")