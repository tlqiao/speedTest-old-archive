from db.mysql_client import execute_query


def get_table_data():
    result = execute_query("select * from post")
    for row in result:
        print(row)


get_table_data()
