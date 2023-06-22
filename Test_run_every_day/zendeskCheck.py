import json
import requests
import pyodbc


class zen_DeskCheck:
    def __init__(self):
        self.orderIdsNotOpned ={}

    def send_to_slack(self,my_dict_lupa):
            #takalot_shotfot_channel = "https://hooks.slack.com/services/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"
            monitor_hazmanot_channel = "https://hooks.slack.com/services/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"
            payload = self.json_to_slack_message(my_dict_lupa)
            requests.post(monitor_hazmanot_channel,data=payload)
            
    def json_to_slack_message(self,list):
            value_list = "\n".join([f"• <https://lupa.zendesk.com/agent/tickets/{ticketId}| {orderId}>" for orderId, ticketId in list.items()])

            # Build the Slack message blocks
            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "מצאתי כמה הזמנות חיוב נכשל שלא היה להם טיקט ופתחתי :pray:"  
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": value_list
                    }
                }
            ]

            # Build the Slack message payload
            payload = {
                "blocks": blocks
            }

            # Convert the payload to JSON and return it
            return json.dumps(payload)
    
    def sendZenDesk(self,orderId,userMail):
        url = "https://lupa.zendesk.com/api/v2/tickets.json" 
        auth = ('odelia@lupa.co.il/token', 'IqnKS4qgiwIU2BfEqkFK3j76rQwNeZr7gCDKPlvh')
        payload = {
            "ticket": {
                "subject": "מספר הזמנה "+str(orderId)+" נעצרה בעקבות תקלת חיוב ",
                "comment": {
                    "body": "auto message from lupa admin"
                },
                "requester":{
                     "email":f"{userMail}"
                }
            }
        }
        headers = {
        "Content-Type": "application/json"
        }

        json_payload = json.dumps(payload)
        response = requests.post(url, data=json_payload,auth=auth,headers=headers)
        response_object = response.json()
        ticket_id = response_object['ticket']['id']
        return ticket_id

    def getAllOrders(self):
        server = '104.155.49.95'
        database = 'master'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute('''
SELECT [order_id],order_date,(select [user_email] FROM [lupa].[dbo].[user_master] where l.master_id=master_id)as e FROM [lupa_online].[dbo].[orders_tbl]as l WHERE in_status = 14
        --AND [order_date] >= DATEADD(HOUR, -24, GETDATE())
        union
        select [order_id],order_date,(select [user_email] FROM [lupa].[dbo].[user_master] where l.master_id=master_id)as e  from lupa_square.dbo.[orders_tbl]as l   WHERE in_status = 14
        --AND [order_date] >= DATEADD(HOUR, -24, GETDATE())
        union
        SELECT o.[a_num] as order_id,
        [order_date],(select [user_email] FROM [lupa].[dbo].[user_master] where oe.order_customer_id=user_id)as e 
        FROM [lupa].[dbo].[orders_tbl]  as o  left join lupa.dbo.[orders_extra_data_tbl] as oe on o.a_num=oe.a_num 
        where in_status=\'%charge failed%\'  --AND [order_date] >= DATEADD(HOUR, -24, GETDATE())
        order by order_date desc''')
        rows = cursor.fetchall()
        for row in rows:
            if not self.isZendeskTicket(row[0]):
                userMail = row[2]
                ticketID= self.sendZenDesk(row[0],userMail)
                self.orderIdsNotOpned[row[0]]=ticketID
        if len(self.orderIdsNotOpned)>0:
            self.send_to_slack(self.orderIdsNotOpned)



        
    def isZendeskTicket(self,orderId):
        url = 'https://lupa.zendesk.com/api/v2/search.json'
        params = {
            #'query': 'מספר הזמנה '+str(orderId)+' נעצרה בעקבות תקלת חיוב',
            'query': str(orderId),
            'type' :'ticket',
            'sort_by': 'created_at',
            'sort_order': 'desc'
        }
        auth = ('odelia@lupa.co.il/token', 'IqnKS4qgiwIU2BfEqkFK3j76rQwNeZr7gCDKPlvh')
        response = requests.get(url, params=params, auth=auth)
        response_object = response.json()
        l  = len(response_object["results"])
        if l == 0:
            return False
        else:
            return True


z = zen_DeskCheck()
z.getAllOrders()
#z.sendZenDesk(111)