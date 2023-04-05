import pandas as pd
from db_connect import cursor
# from transform_senstive import new_table


# TODO Could improve the documentation of how this functionality works - be more specific so its easier to find "at what part does exactly what"


class Transactions:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    # Executes SQL query and returns list of tuples
    def get_db_id(self, sql_command: str):
        cursor.execute(sql_command)
        db_id = cursor.fetchall()
        return db_id

    # Transforms DataFrame: replaces store names by store DB indexes; same with customers
    def get_transactions_fk(self, table: str, column_name: str, db_col1_name: str, db_col2_name: str):
        new_row_vals = []
        for _, row in self.df.iterrows():
            val = row[column_name].strip()
            query = f"SELECT {db_col1_name} FROM {table} WHERE {db_col2_name} = '{val}' LIMIT 1"
            trns_id = self.get_db_id(query)[0][0]
            new_row_vals.append(trns_id)
        new_df = pd.DataFrame({column_name: new_row_vals})
        self.df.update(new_df)

    def get_transactions_df(self):
        self.get_transactions_fk("stores", "store", "store_id", "store_name")
        self.get_transactions_fk("customers", "customer_name",
                                 "customer_id", "customer_name")
        df = self.df[["timestamp", "store",
                      "customer_name", "cash_or_card", "total_price"]]
        df.columns = ["date_and_time", "store_id",
                      "customer_id", "payment_type", "order_price"]
        return df
