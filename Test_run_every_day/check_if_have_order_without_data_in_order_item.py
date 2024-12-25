import pyodbc
import requests

class OrderChecker:
    def __init__(self, conn_string, slack_webhook_url):
        self.conn_string = conn_string
        self.slack_webhook_url = slack_webhook_url

    def fetch_orders_without_items(self):
        query = """
        SELECT order_id
        FROM [lupa_square].[dbo].[orders_tbl] a
        WHERE a.in_status = 21 AND NOT EXISTS (
            SELECT 1
            FROM [lupa_square].[dbo].[order_item_tbl] b
            WHERE b.order_id = a.order_id
        );
        """
        try:
            with pyodbc.connect(self.conn_string) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                orders = cursor.fetchall()
                return orders
        except Exception as e:
            print(f"An error occurred while fetching orders: {e}")
            return []

    def send_slack_notification(self, orders):
        if not orders:
            print("No orders found without corresponding data in order_item_tbl.")
            return

        order_ids = ", ".join(str(order[0]) for order in orders)
        message = f"Have orders without data in order_item_tbl: {order_ids}"

        try:
            response = requests.post(
                self.slack_webhook_url,
                json={"text": message},
                headers={"Content-Type": "application/json"},
            )
            if response.status_code == 200:
                print("Message sent to Slack successfully.")
            else:
                print(f"Failed to send message to Slack: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"An error occurred while sending Slack notification: {e}")

    def check_and_notify(self):
        orders = self.fetch_orders_without_items()
        self.send_slack_notification(orders)

if __name__ == "__main__":
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=104.155.49.95;"  # Replace with your server name
        "DATABASE=lupa_square;"  # Replace with your database name
        "UID=MachineDBA;"  # Replace with your username
        "PWD=Kk28!32Zx;"  # Replace with your password
    )

    slack_webhook_url = "https://hooks.slack.com/services/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"  # Replace with your Slack webhook URL

    checker = OrderChecker(conn_string, slack_webhook_url)
    checker.check_and_notify()