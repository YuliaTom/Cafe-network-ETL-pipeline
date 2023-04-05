from db_connect import cursor, db

# CREATING ALL THE TABLES INTO THE DATABASE

# CREATE PRODUCT TABLE


def create_products():
    create_script = '''CREATE TABLE IF NOT EXISTS Products(
                    product_id      INT identity(1, 1) PRIMARY KEY NOT NULL,
                    size            varchar(50),
                    product_name    varchar(50) NOT NULL,
                    flavour         varchar(50),
                    price           float(5) NOT NULL,
                    CONSTRAINT dup_prod_check UNIQUE (product_name, size, flavour, price))'''
    cursor.execute(create_script)

# CREATE BASKET TABLE


def create_baskets():
    create_script = '''CREATE TABLE IF NOT EXISTS Baskets(
                    product_id INT NOT NULL,
                    transaction_id INT NOT NULL,                   
                    FOREIGN KEY (product_id)
                        REFERENCES products (product_id),
                    FOREIGN KEY (transaction_id)
                        REFERENCES transactions (transaction_id))'''
    cursor.execute(create_script)


# CREATE TRANSACTION TABLE

def create_transactions():
    create_script = '''CREATE TABLE IF NOT EXISTS Transactions(
                    transaction_id  INT identity(1, 1) PRIMARY KEY NOT NULL,
                    date_and_time   TIMESTAMP NOT NULL,
                    store_id        INT NOT NULL,
                    customer_id     INT NOT NULL,
                    payment_type     varchar(50) NOT NULL,
                    order_price     float(5) NOT NULL,
                    FOREIGN KEY (store_id)
                        REFERENCES stores (store_id),
                    FOREIGN KEY (customer_id)
                        REFERENCES customers (customer_id),
                    CONSTRAINT dup_tran_check UNIQUE (date_and_Time, store_id, customer_id, payment_type, order_price));
                    SET datestyle = dmy;'''
    cursor.execute(create_script)


# CREATE STORE TABLE


def create_stores():
    create_script = '''CREATE TABLE IF NOT EXISTS Stores(
                    store_id    INT identity(1, 1) PRIMARY KEY NOT NULL,
                    store_name  varchar(50) NOT NULL,
                    CONSTRAINT dup_store_check UNIQUE (store_name))'''
    cursor.execute(create_script)


# CREATE CUSTOMER TABLE


def create_customers():
    create_script = '''CREATE TABLE IF NOT EXISTS Customers(
                    customer_id     INT identity(1, 1) PRIMARY KEY NOT NULL,
                    customer_name   VARCHAR,
                    card_number     VARCHAR,
                    CONSTRAINT dup_cust_check UNIQUE (customer_name, card_number))'''
    cursor.execute(create_script)
