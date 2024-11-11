import re
from playwright.sync_api import sync_playwright, expect
from slack import send_slack
from data_base import *




def test_error_insufficient():
    command = "select * from [social].[dbo].[smartbook_tbl] where progress = -1 and error_ex = 'insufficient system resources' order by error_date desc"
    data = mysql(command)


    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "insufficient system resources",
                "emoji": True
            }
        },
        {
            "type": "divider"
        }
    ]
    if data:
        send_slack(blocks, "post_online", "#system-monitor")