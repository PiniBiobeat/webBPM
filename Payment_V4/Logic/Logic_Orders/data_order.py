# from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from data_base import mysql, postgres_env


class DataConnection:

    def orders_tbl(self,order_number):
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
        FROM [lupa_online].[dbo].[orders_tbl] 
        WHERE order_id = {order_number}
        """
        data_command = mysql(command)
        if not data_command:
            raise ValueError(f"No data found for order ID {order_number}")
        return data_command[0]




    def total_discount_sum(self,order_number):
        command = f"select SUM(discount_actual_value) FROM cpn.coupon_tbl x WHERE x.use_date is not null and order_id = {order_number}"
        data_command = postgres_env(command)
        if not data_command[0]:
            return None
        else:
            return print(data_command[0][0])







# DataConnection().total_discount_sum("7824149")






# 7823844

