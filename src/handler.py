import pandas as pd
from transform_senstive_info import HashInformation
from load_data import load_baskets_to_db, load_customers_to_db, load_products_to_db, load_stores_to_db, load_transactions_to_db
from transactions import Transactions
from transform_basket import TransformBasket
from basket_class import Basket
from create_tables import *


def main(df):

    # Create tables in the correct order checking for duplicates

    create_products()
    create_stores()
    create_customers()
    create_transactions()
    create_baskets()

    print("Tables successfully created.\n")

    # Transform the DATA by hashing customer names and card numbers

    hash_object = HashInformation(df)
    hash_object.test_column_names()
    hash_dataframe = hash_object.return_hashed_df()

    # Continue transforming dataframe by creating a TransformBasket instance

    transform_object = TransformBasket(df)

    # Calling TransformBasket functions to get dataframes with unique rows only

    products = transform_object.get_unique_prod_df()
    stores = transform_object.get_unique_stores()
    customers = transform_object.get_unique_customers()

    """ 
    Load dataframe to database. 
    Here each row of a dataframe gets compared to existing rows on database and only unique ones are inserted into DB tables.
    """

    load_products_to_db(db, products, 'products')
    print("Suscessfully loaded 'products'.\n")

    load_customers_to_db(db, customers, 'customers')
    print("Suscessfully loaded 'customers'.\n")

    load_stores_to_db(db, stores, 'stores')
    print("Suscessfully loaded 'stores'.\n")

    # Get foreign keys from the customers, products and stores tables to load into a transactions table

    transaction_object = Transactions(df)
    transaction_dataframe = transaction_object.get_transactions_df()

    # Load clean dataframe to transations table

    load_transactions_to_db(db, transaction_dataframe, 'transactions')
    print("Suscessfully loaded 'transactions'\n")

    # Load basket dataframe into basket table

    basket_object = Basket(hash_dataframe)
    basket_df = basket_object.get_basket_fk(transaction_dataframe)
    load_baskets_to_db(db, basket_df, 'baskets')
    print("Suscessfully loaded 'baskets'\n")
    return "Lambda ran suscessfully"
