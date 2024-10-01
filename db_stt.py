import sqlite3
from config_stt import DB_NAME, TABLE_NAME


def create_db(database_name=DB_NAME):
    db_path = f'{database_name}'
    conn = sqlite3.connect(db_path)
    conn.close()


def execute_query(sql_query, data=None, db_path=DB_NAME):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        if data:
            cursor.execute(sql_query, data)
        else:
            cursor.execute(sql_query)
        connection.commit()


def execute_selection_query(sql_query, data=None, db_path=DB_NAME):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    if data:
        cursor.execute(sql_query, data)
    else:
        cursor.execute(sql_query)
    rows = cursor.fetchall()
    connection.close()
    return rows


def create_table(TABLE_NAME):
    sql_query = (f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                 f'(id INTEGER PRIMARY KEY,'
                 f'user_id INTEGER,'
                 f'stt_blocks INTEGER)')
    execute_query(sql_query)


def insert_row(user_id, sst_blocks):
    sql_query = f"""
    INSERT INTO {TABLE_NAME} 
    (user_id, stt_blocks)
    VALUES(?,?)"""
    execute_query(sql_query, [user_id, sst_blocks])


def count_all_blocks(user_id):
    sql_query = f"""
    SELECT SUM(stt_blocks)
    FROM {TABLE_NAME}
    WHERE user_id = "{user_id}"
    GROUP BY user_id
    """
    data = execute_selection_query(sql_query)

    if data:
        return data[0][0]


def prepare_db():
    create_db()
    create_table(TABLE_NAME)
