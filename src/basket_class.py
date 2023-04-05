import pandas as pd
from transform_basket import TransformBasket
from db_connect import cursor
from datetime import datetime

# TODO Improve readibility


class Basket:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        trans_basket = TransformBasket(self.df)
        self.baskets = trans_basket.get_product_list()

    def get_db_id(self, sql_command: str):
        cursor.execute(sql_command)
        db_id = cursor.fetchall()
        return db_id

    def get_basket_fk(self, transaction_df: pd.DataFrame):
        trans_fk_list = []
        prod_fk_list_of_lists = []
        for _, row in transaction_df.iterrows():
            date_and_time = datetime.strptime(
                row["date_and_time"].strip(), "%d/%m/%Y %H:%M")
            store_id = row["store_id"]
            customer_id = row["customer_id"]
            payment_type = row["payment_type"].strip()
            order_price = row["order_price"]
            trns_id_sql = f"SELECT transaction_id FROM transactions WHERE date_and_time = '{date_and_time}' AND store_id = {store_id} AND customer_id = {customer_id} AND payment_type = '{payment_type}' AND order_price= '{order_price}'"
            trns_id = self.get_db_id(trns_id_sql)[0][0]
            trans_fk_list.append(trns_id)
        for basket in self.baskets:
            prod_fk_list = []
            for product in basket:
                f_selection = ""
                if product.flavour != '':
                    f_selection = f"AND flavour = '{product.flavour}'"
                prod_id_sql = f"SELECT product_id FROM products WHERE product_name = '{product.name}' AND size = '{product.size}' {f_selection} AND price = '{product.price}'"
                prod_id = self.get_db_id(prod_id_sql)[0][0]
                prod_fk_list.append(prod_id)
            prod_fk_list_of_lists.append(prod_fk_list)
        basket_df = pd.DataFrame(
            {"transaction_id": trans_fk_list, "product_id": prod_fk_list_of_lists})
        basket_df = basket_df.explode("product_id")
        return basket_df
