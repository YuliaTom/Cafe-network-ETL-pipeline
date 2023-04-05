import hashlib
import pandas as pd


class HashInformation:
    def __init__(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df
        self.column_names = ['timestamp', 'store', 'customer_name',
                             'basket_items', 'total_price', 'cash_or_card', 'card_number']

    def hash_card(self, fieldname):
        # select and convert one column to string
        self.df[fieldname] = self.df[fieldname].astype(str)
        # float card fix, removes .0
        self.df[fieldname] = self.df[fieldname].apply(
            lambda x: x[:-2] if x[-2:] == ".0" else x)
        # convert card number into hash and skip nan values
        self.df[fieldname] = self.df[fieldname].apply(
            lambda x: hashlib.sha256(x.encode()).hexdigest() if x != 'nan' else None)
        hash_column = self.df[fieldname]
        return hash_column

    def hash_name(self, fieldname):
        # convert name into hash and skip nan values

        self.df[fieldname] = self.df[fieldname].astype(str)
        self.df[fieldname] = self.df[fieldname].apply(
            lambda x: hashlib.sha256(x.encode()).hexdigest() if x != 'nan' else x)
        hash_column = self.df[fieldname]
        return hash_column

    def test_column_names(self):
        while True:
            try:
                assert list(self.df.columns) == self.column_names
                self.df['card_number'] = self.hash_card('card_number')
                # print(df['card_number'])
                self.df['customer_name'] = self.hash_name('customer_name')
                # print(df['customer_name'])

                break
            except AssertionError:
                print('column names do not match')
                break

    def return_hashed_df(self):
        self.df['customer_name'] = self.hash_name('customer_name')
        return self.df
