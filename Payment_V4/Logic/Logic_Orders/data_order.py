from data_base import mysql, postgres_env
from dotenv import load_dotenv
import configparser
import requests
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.ini')), load_dotenv()

class DataConnection:

    def orders_tbl(self, order_number, db):
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




    def total_discount_sum(self,order_number):
        command = f"select SUM(discount_actual_value) FROM cpn.coupon_tbl x WHERE x.use_date is not null and order_id = {order_number}"
        data_command = postgres_env(command)
        if not data_command[0][0]:
            return None
        else:
            return data_command[0][0]

# DataConnection().total_discount_sum("7824652")
# 7823844


class order_detail:

    def clear_basket_before_tests(self):
        master_id = config['GLOBAL']['paymentV4_test_master_id']
        #delete book
        command = f"SELECT [item_id] FROM [lupa_online].[dbo].[order_item_tbl] where master_id = {master_id} and in_status = 1"
        get_item_list = mysql(command)
        item_ids = ','.join(str(item[0]) for item in get_item_list)
        url = f"https://paymentsv4-api.lupa.co.il/api.aspx?method=delete_item&item_ids=[{item_ids}]&source_type=books&language=&platform=books&device=null&source_device=web&token=PFKEcRIKrw_c5z4ZU7mdE7Za0BB3oCrj7HKluDxZuGZK2pKOrcP8iaC2FBDa0rhniY9pioC4gENdgemaSpj-0NLbbeO2ZkUnVBlomwoR3NjJfHChdEX-3B9aXd3YHe5gaoAd3SXTfdxBNYsX7q3ZglGJy6xTdr4E5qpvJcez_H7_FqprpEaKqiD8V3fD0HrRmAhNqHfuIpDpFx4rmff5XUqwXcbJkjf3njLFpJyMy4ScQ9lDACM2raQl8uVbhMM-j0SVArzQylzHNyesPlOUxo_2dwAP_0k6S_Sh-AjAJ2BLUtFvy9fbETZ9RO6KDlM-oKoU6qHdtCTZB9Ts-34JeQ2&show_header="
        requests.get(url)
        #delete tiles
        command2 = f"SELECT [item_id] FROM [lupa_square].[dbo].[order_item_tbl] where master_id = {master_id} and in_status = 1"
        get_item_list2 = mysql(command2)
        item_ids = ','.join(str(item[0]) for item in get_item_list2)
        url2 = f"https://paymentsv4-api.lupa.co.il/api.aspx?method=delete_item&item_ids=[{item_ids}]&source_type=tiles&language=&platform=books&device=null&source_device=web&token=PFKEcRIKrw_c5z4ZU7mdE7Za0BB3oCrj7HKluDxZuGZK2pKOrcP8iaC2FBDa0rhniY9pioC4gENdgemaSpj-0NLbbeO2ZkUnVBlomwoR3NjJfHChdEX-3B9aXd3YHe5gaoAd3SXTfdxBNYsX7q3ZglGJy6xTdr4E5qpvJcez_H7_FqprpEaKqiD8V3fD0HrRmAhNqHfuIpDpFx4rmff5XUqwXcbJkjf3njLFpJyMy4ScQ9lDACM2raQl8uVbhMM-j0SVArzQylzHNyesPlOUxo_2dwAP_0k6S_Sh-AjAJ2BLUtFvy9fbETZ9RO6KDlM-oKoU6qHdtCTZB9Ts-34JeQ2&show_header="
        requests.get(url2)
