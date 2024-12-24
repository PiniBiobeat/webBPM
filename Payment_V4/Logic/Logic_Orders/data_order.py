# from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from data_base import mysql


class DataConnection:

    def orders_tbl(self):
        command = """
        SELECT [order_id]
              ,[master_id]
              ,[in_status]
              ,[total_items_quantity]
              ,[total_items_price]
              ,[total_order_price]
              ,[discount_admin_value]
              ,[discount_checkout_value]
              ,[shipping_value]
              ,[shipping_method]
              ,[invoice_number]
        FROM [lupa_online].[dbo].[orders_tbl] 
        WHERE order_id = 7823898
        """
        data_command = mysql(command)
        order_id, master_id, in_status, total_items_quantity, total_items_price, total_order_price, discount_admin_value, \
        discount_checkout_value, shipping_value, shipping_method, invoice_number = data_command[0]
        print(order_id)
        return order_id, master_id, in_status, total_items_quantity, total_items_price, total_order_price, \
               discount_admin_value, discount_checkout_value, shipping_value, shipping_method, invoice_number



# DataConnection().orders_tbl()
