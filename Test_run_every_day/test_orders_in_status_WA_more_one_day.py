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
            message += f"Database: {database_name}, Order ID: {order_id}, Status: {in_status}\n"
        send_to_slack(message)
    else:
         print(f"No orders with 'charged_date' older than 1 day found (Checked on {datetime.now()}).")




