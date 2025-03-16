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
# Create a connection to SQL Server
def get_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    return conn


# Function to execute the provided query and fetch results
def fetch_orders():
    query = """
        SELECT 
            order_id, 
            master_id, 
            in_status, 
            charged_date, 
            device 
        FROM 
            [lupa_online].[dbo].[orders_tbl] 
        WHERE 
            in_status = 0 
            AND DATEADD(day, -1, GETDATE()) > charged_date; 
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
        message = f"Orders with 'in_status = 0':\n"
        for row in rows:
            order_id, master_id, in_status, charged_date, device = row
            message += f"Order ID: {order_id}, Master ID: {master_id}, Status: {in_status}, Charged Date: {charged_date}, Device: {device}\n"

        send_to_slack(message)
    else:
        print(
            f"No orders with 'in_status = 0' and 'charged_date' older than 1 day found (Checked on {datetime.now()}).")


