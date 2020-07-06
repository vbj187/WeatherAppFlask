import sqlite3

db_name = 'database.db'


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
        return None


def run_query(sql_query, args=[]):
    conn = create_connection(db_name)
    cur = conn.cursor()
    cur.execute(sql_query, args)


def create_table():
    sql_query = """create table if not exists cities(
        id INTEGER PRIMARY KEY,
        url text,
        website_text text
    );
    """
    run_query(sql_query)


if __name__ == '__main__':
    create_connection(db_name)
    create_table()
