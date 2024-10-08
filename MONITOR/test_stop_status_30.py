from data_base import *


def test_stop_status_30():
    select_query = "select [order_id],[master_id],[tree_version],[insert_date] from [lupa_online].[dbo].[order_item_tbl] where in_status = 30  AND DATEADD(MINUTE, 5, insert_date) < GETDATE() AND DATEADD(MINUTE, 6, insert_date) > GETDATE();"
    data = mysql(select_query)
    print("\n")
    temp_list = []
    for row in data:
        order_id, master_id, tree_version, insert_date = row
        link = f"<https://admin.lupa.co.il/admin_online/Order_Details.aspx?id={order_id}|{order_id}>"
        temp = f"• Order: {link}  Master: {master_id}   Version: {tree_version}   date: *{insert_date}*"
        temp_list.append(temp)

    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":loading: *הזמנות שתקועות מעל 5 דקות בסטטוס 30* :loading:",
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n".join(temp_list)
            }
        }
    ]



    if not temp_list == []:
        send_slack(block)