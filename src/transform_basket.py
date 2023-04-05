from product import Product
import pandas as pd
from typing import List


# TODO  A little more documentation on exactly how this functionality works would be a welcomed improvment


class TransformBasket:
    def __init__(self, df: pd.DataFrame) -> List[List[Product]]:
        self.df = df

    def get_product_baskets(self):
        basket_items_list = []
        basket_items = self.df["basket_items"]
        for item in basket_items:
            basket_items_list.append(item.split(","))
        return basket_items_list

    # Returns a list of basket Product objects

    def get_product_list(self):
        basket_items_list = self.get_product_baskets()
        baskets_list = []
        for alist in basket_items_list:
            product_list = []
            for item in alist:
                size = item.split()[0].title()
                price = item.split("-")[-1]
                long_name = item.split("-")[0].lower().lstrip()
                if len(item.split("-")) == 3:
                    flavour = item.split("-")[1]
                else:
                    flavour = ""
                if "flavoured" in long_name:   # Finds product name between "flavoured" and "-"
                    name = long_name[long_name.find(
                        "flavoured") + 9:].strip().title()   # Clear white spaces
                else:
                    name = " ".join(long_name.split(" ")[1:]).title()
                product_list.append(
                    Product(name.strip(), price.strip(), size.strip(), flavour.strip()))
            baskets_list.append(product_list)
        return baskets_list

    # Returns unique products based on name+size+flafour+price
    def get_unique_products(self) -> List[Product]:
        product_set = set()
        for basket in self.get_product_list():
            for product in basket:
                product_set.add(product)
        return list(product_set)

    # Returns DataFrame of unique products
    def get_unique_prod_df(self) -> pd.DataFrame:
        df = pd.DataFrame(
            [product_attrib.__dict__ for product_attrib in self.get_unique_products()])
        return df.rename(columns={"name": "product_name"})

    def get_unique_stores(self) -> pd.DataFrame:
        unique_stores_list = self.df["store"].unique()
        df = pd.DataFrame(unique_stores_list)
        df.columns = ['store_name']
        return df

    def get_unique_customers(self) -> pd.DataFrame:
        unique_customers = self.df[["customer_name", "card_number"]].drop_duplicates(
            subset=["customer_name", "card_number"],
            keep='last').reset_index(drop=True)
        return unique_customers
