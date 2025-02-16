from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from data_base import mysql, postgres_env
from dotenv import load_dotenv
import configparser
import requests
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.ini')), load_dotenv()
master_id = config['GLOBAL']['paymentV4_test_master_id']


class DataConnection:

    def orders_tbl(self, order_number):
        db = Generalfunction.source_db_data
        command = f"""
        SELECT [order_id]
              ,[master_id]
              ,[in_status]
              ,[total_items_quantity]
              ,[total_items_price]
              ,[total_order_price]
              ,[shipping_value]
              ,[shipping_method]
              ,[invoice_number]
        FROM [{db}].[dbo].[orders_tbl] 
        WHERE order_id = {order_number}
        """
        data_command = mysql(command)
        if not data_command:
            raise ValueError(f"No data found for order ID {order_number}")
        return data_command[0]


    def total_discount_sum(self, order_number):
        command = f"select SUM(discount_actual_value) FROM cpn.coupon_tbl x WHERE x.use_date is not null and order_id = {order_number}"
        data_command = postgres_env(command)
        if not data_command[0][0]:
            return None
        else:
            return data_command[0][0]


# DataConnection().total_discount_sum("7824652")
# 7823844


class ClearBasketApi:

    def clear_basket_before_tests(self):
        # delete book
        command = f"SELECT [item_id] FROM [lupa_online].[dbo].[order_item_tbl] where master_id = {master_id} and in_status = 1"
        get_item_list = mysql(command)
        item_ids = ','.join(str(item[0]) for item in get_item_list)
        url = f"https://paymentsv4-api.lupa.co.il/api.aspx?method=delete_item&item_ids=[{item_ids}]&source_type=books&language=&platform=books&device=null&source_device=web&token=PFKEcRIKrw_c5z4ZU7mdE7Za0BB3oCrj7HKluDxZuGZK2pKOrcP8iaC2FBDa0rhniY9pioC4gENdgemaSpj-0NLbbeO2ZkUnVBlomwoR3NjJfHChdEX-3B9aXd3YHe5gaoAd3SXTfdxBNYsX7q3ZglGJy6xTdr4E5qpvJcez_H7_FqprpEaKqiD8V3fD0HrRmAhNqHfuIpDpFx4rmff5XUqwXcbJkjf3njLFpJyMy4ScQ9lDACM2raQl8uVbhMM-j0SVArzQylzHNyesPlOUxo_2dwAP_0k6S_Sh-AjAJ2BLUtFvy9fbETZ9RO6KDlM-oKoU6qHdtCTZB9Ts-34JeQ2&show_header="
        requests.get(url)
        # delete tiles
        command2 = f"SELECT [item_id] FROM [lupa_square].[dbo].[order_item_tbl] where master_id = {master_id} and in_status = 1"
        get_item_list2 = mysql(command2)
        item_ids = ','.join(str(item[0]) for item in get_item_list2)
        url2 = f"https://paymentsv4-api.lupa.co.il/api.aspx?method=delete_item&item_ids=[{item_ids}]&source_type=tiles&language=&platform=books&device=null&source_device=web&token=PFKEcRIKrw_c5z4ZU7mdE7Za0BB3oCrj7HKluDxZuGZK2pKOrcP8iaC2FBDa0rhniY9pioC4gENdgemaSpj-0NLbbeO2ZkUnVBlomwoR3NjJfHChdEX-3B9aXd3YHe5gaoAd3SXTfdxBNYsX7q3ZglGJy6xTdr4E5qpvJcez_H7_FqprpEaKqiD8V3fD0HrRmAhNqHfuIpDpFx4rmff5XUqwXcbJkjf3njLFpJyMy4ScQ9lDACM2raQl8uVbhMM-j0SVArzQylzHNyesPlOUxo_2dwAP_0k6S_Sh-AjAJ2BLUtFvy9fbETZ9RO6KDlM-oKoU6qHdtCTZB9Ts-34JeQ2&show_header="
        requests.get(url2)


    def clear_coupons_before_tests(self):
        command_coupon = f"SELECT mng.cancel_coupons_by_user_id({master_id});"
        postgres_env(command_coupon)




class DataPriceList:

    def check_price_list(self, return_base_price):
        source_db = Generalfunction.source_db_data
        command_get_catalog_code_quantity = f"""
            SELECT 
                [{source_db}].[dbo].[order_item_catalog_code].[catalogue_code],
                [{source_db}].[dbo].[order_item_tbl].[quantity]
            FROM 
                [{source_db}].[dbo].[order_item_catalog_code]
            LEFT JOIN 
                [{source_db}].[dbo].[order_item_tbl]
            ON 
                [{source_db}].[dbo].[order_item_tbl].[item_id] = [{source_db}].[dbo].[order_item_catalog_code].[item_id]
            WHERE 
            [{source_db}].[dbo].[order_item_catalog_code].[master_id] = {master_id} 
            AND 
            [{source_db}].[dbo].[order_item_tbl].[in_status] = 1
        """
        catalogue_data = mysql(command_get_catalog_code_quantity)
        total_sum = sum(
            result[0][0] for record in catalogue_data
            if (result := postgres_env(f"""
                SELECT sum(pt.base_price * {record[1]})
                FROM prc.pricelist_tbl AS pt
                WHERE id = '{record[0]}'
            """)) and result[0][0] is not None)
        print(f"fist base price was: {total_sum}")
        assert return_base_price == total_sum
