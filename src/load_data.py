import psycopg2
import psycopg2.extras as extras
from datetime import datetime


def execute_sql(connection, df, table, tuples):
    cursor = connection.cursor()
    cols = ','.join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    try:
        extras.execute_values(cursor, query, tuples)
        connection.commit()
        print("The table has been uploaded to db.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        connection.rollback()
        cursor.close()
        return 1
    cursor.close()


def load_products_to_db(connection, df, table):
    cursor = connection.cursor()
    tuples = []
    for row in df.to_numpy():
        temp_row = row
        if row[-1] == "":
            sql = f"SELECT * FROM {table} WHERE product_name = %s AND price = %s AND size = %s AND (flavour IS NULL OR flavour = '')"
            temp_row = temp_row[:-1]
        else:
            sql = f"SELECT * FROM {table} WHERE product_name = %s AND price = %s AND size = %s AND flavour = %s"
        cursor.execute(sql, tuple(temp_row))
        exist_check = cursor.fetchone()
        if exist_check == None:
            tuples.append(tuple(row))
    execute_sql(connection, df, table, tuples)


def load_baskets_to_db(connection, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    execute_sql(connection, df, table, tuples)


def load_stores_to_db(connection, df, table):
    cursor = connection.cursor()
    tuples = []
    for row in df.to_numpy():
        sql = f"SELECT * FROM {table} WHERE store_name = %s"
        cursor.execute(sql, tuple(row))
        exist_check = cursor.fetchone()
        if exist_check == None:
            tuples.append(tuple(row))
    execute_sql(connection, df, table, tuples)


def load_customers_to_db(connection, df, table):
    cursor = connection.cursor()
    tuples = []
    for row in df.to_numpy():
        temp_row = row
        if row[-1] == "" or row[-1] == None:
            sql = f"SELECT * FROM {table} WHERE customer_name = %s AND (card_number IS NULL OR card_number = '')"
            temp_row = temp_row[:-1]
        else:
            sql = f"SELECT * FROM {table} WHERE customer_name = %s AND card_number = %s"
        cursor.execute(sql, tuple(temp_row))
        exist_check = cursor.fetchone()
        if exist_check == None:
            tuples.append(tuple(row))
    execute_sql(connection, df, table, tuples)


def load_transactions_to_db(connection, df, table):
    cursor = connection.cursor()
    tuples = []
    for row in df.to_numpy():
        date_and_time = datetime.strptime(
            row[0].strip(), "%d/%m/%Y %H:%M")
        store_id = row[1]
        customer_id = row[2]
        payment_type = row[3].strip()
        order_price = row[4]
        sql = f"SELECT * FROM transactions WHERE date_and_time = '{date_and_time}' AND store_id = {store_id} AND customer_id = {customer_id} AND payment_type = '{payment_type}' AND order_price= '{order_price}'"
        cursor.execute(sql, row)
        exist_check = cursor.fetchone()
        if exist_check == None:
            tuples.append(tuple(row))
    execute_sql(connection, df, table, tuples)
