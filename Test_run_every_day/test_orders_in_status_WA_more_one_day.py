import pyodbc
import requests
from datetime import datetime

# Define your SQL Server connection details
server = '104.155.49.95'
username = 'MachineDBA'
password = 'Kk28!32Zx'
database = 'lupa_online'  # Any valid database to establish the connection
slack_webhook_url = 'https://hooks.slack.com/services/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'  # Replace with your Slack webhook URL

# Create a connection to SQL Server
def get_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    return conn

def insert_to_table_error(order_id, master_id, platform, payload, code, insert_date):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = '''INSERT INTO lupa.[dbo].orders_generic_errors_tbl (order_id, master_id, platform, payload, code, insert_date)
                   VALUES (?, ?, ?, ?, ?, ?);'''
        cursor.execute(query, (order_id, master_id, platform, payload, code, insert_date))
        cursor.commit()
        cursor.close()
        conn.close()
        print("Insert successful!")
    except Exception as e:
        print(f"Error: {e}")
def order_exists(order_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = '''SELECT COUNT(*) FROM lupa.[dbo].orders_generic_errors_tbl WHERE order_id = ?'''
        cursor.execute(query, (order_id,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count > 0
    except Exception as e:
        print(f"Error checking order existence: {e}")
        return False

# Function to execute the provided query and fetch results
def fetch_orders():
    query = """
    -- Query for Database 1 (local instance)
    SELECT 'Database1' AS DatabaseName, order_id, in_status
    FROM [lupa_online].[dbo].[orders_tbl]
    WHERE in_status = 26 AND DATEDIFF(DAY, charged_date, GETDATE()) > 1

    UNION ALL

    -- Query for Database 2 (Linked Server)
    SELECT 'Database2' AS DatabaseName, order_id, in_status
    FROM [lupa_square].[dbo].[orders_tbl]
    WHERE in_status = 26 AND DATEDIFF(DAY, charged_date, GETDATE()) > 1
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return []


# Function to send results to Slack
def send_to_slack(message):
    payload = {"text": message}
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code == 200:
        print("Successfully sent to Slack!")
    else:
        print(f"Failed to send message to Slack: {response.status_code}, {response.text}")


# Main function to fetch data and send it to Slack
def test_check_orders_and_notify():
    rows = fetch_orders()

    if rows:
        message = f"Orders with 'charged_date' older than 1 day (Checked on {datetime.now()}):\n"
        for row in rows:
            database_name, order_id, in_status = row
            if not order_exists(order_id):
                insert_to_table_error(order_id, None, None, None, in_status, datetime.now())
                message += f"Database: {database_name}, Order ID: {order_id}, Status: {in_status}\n"
                send_to_slack(message)
    else:
         print(f"No orders with 'charged_date' older than 1 day found (Checked on {datetime.now()}).")




