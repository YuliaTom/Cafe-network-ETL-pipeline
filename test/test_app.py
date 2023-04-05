import unittest.mock
from unittest.mock import patch
from ..src.transform_basket import TransformBasket
import pandas as pd
# from ..src.product import Product
from ..src.transform_senstive_info import HashInformation


# content of test_sample.py


class TestMyClass(unittest.TestCase):
    @patch('transform_basket.TransformBasket.get_product_list')
    def test_get_unique_products(self, mock_get_product_list):
        mock_product_list = [
            [Product("Test 1", 1, "Large"), Product("Test 2", 1, "Large")], [Product("Test 1", 1, "Large")]]
        mock_get_product_list.return_value = mock_product_list

        transform_basket = TransformBasket(pd.DataFrame)
        actual = transform_basket.get_unique_products()
        expected_products = [
            Product("Test 1", 1, "Large"), Product("Test 2", 1, "Large")]
        self.assertCountEqual(expected_products,  actual)

    def test_get_unique_stores():

        store_list = {"store": ["Uppingham",
                                "Chesterfield", "Longfield", "Uppingham"]}
        unique_store_list = {"store_name": [
            "Uppingham", "Chesterfield", "Longfield"]}

        df = pd.DataFrame(store_list)
        transformbasket = TransformBasket(df)

        actual = transformbasket.get_unique_stores()
        expected = pd.DataFrame(unique_store_list)
        print(actual)
        print(expected)

        assert actual.equals(expected)

    def test_get_unique_customers():

        customers_name = {"customer_name": ["Wayne", "Shanti", "Yulia", "Shanti", "Callum", "Hardik"],
                          "card_number": [1234, 4321, 5678, 4321, 777, 888]}

        unique_store_customers = {"customer_name": ["Wayne", "Yulia", "Shanti", "Callum", "Hardik"],
                                  "card_number": [1234, 5678, 4321, 777, 888]}

        df = pd.DataFrame(customers_name)
        transformbasket = TransformBasket(df)

        actual = transformbasket.get_unique_customers()
        expected = pd.DataFrame(unique_store_customers)

        assert actual.equals(expected)

    # Testing Card Number

    def test_hashed_card():

        customers_name = {"card_number": [1234]}

        hashed_value = {"card_number": [
            '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4']}

        df = pd.DataFrame(customers_name)
        transformbasket = HashInformation(df)

        actual = transformbasket.hash_card("card_number")
        expected = pd.DataFrame(hashed_value)["card_number"]

        assert actual.equals(expected)

    # Testing Hashed Customer Name

    def test_hashed_customer():

        customers_name = {"customer_name": ["Wayne"]}

        hashed_value = {"customer_name": [
            '3801ab6292b288faf9ca449d4a4029ec30261423162c443d4f72b43945749e04']}

        df = pd.DataFrame(customers_name)
        transformbasket = HashInformation(df)

        actual = transformbasket.hash_card("customer_name")
        expected = pd.DataFrame(hashed_value)["customer_name"]

        assert actual.equals(expected)


if __name__ == '__main__':
    unittest.main()
