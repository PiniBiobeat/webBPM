import re
from playwright.sync_api import sync_playwright, expect
from slack import send_slack
from data_base import *


def test_error_insufficient():
    command = "select * from [social].[dbo].[smartbook_tbl] where error_ex = 'Insufficient system resources'"
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
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<@U03E109PX0R>"
            }
        },
        {
            "type": "divider"
        }
    ]
    if data:
        send_slack(blocks, "post_online", "#system-monitor")
