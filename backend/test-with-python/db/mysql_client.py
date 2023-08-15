import mysql.connector
from configs.load_config import get_configs


def get_database_connection():
    configs = get_configs()["mysqldb"]
    connection = mysql.connector.connect(**configs)
    return connection


def execute_query(query):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def execute_update(query):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    connection.close()
    return affected_rows


def execute_delete(query):
    return execute_update(query)


def execute_insert(query):
    return execute_update(query)

# example for query data from mysql db, define your own sql to get data from db


def get_table_data():
    result = execute_query("select * from posts")
    for row in result:
        print(row)


get_table_data()
