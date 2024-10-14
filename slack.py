import requests



webhook = {
    "paymentv4": {
        "#demo_app": "https://hooks.slack.com/services/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",
        "#order_monitor": "https://hooks.slack.com/services/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",
        "#system_monitor": "https://hooks.slack.com/services/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"
    },
    "demo": {
        "#demo_app": "https://hooks.slack.com/services/T01EPT4V4B0/B07ABC12345/xyz0987654321"
    },
    "App_V3": {
        "#proj_app_v3": "https://hooks.slack.com/services/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",
        "#system-monitor": "https://hooks.slack.com/services/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",
        "#demo_app": "https://hooks.slack.com/services/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"

    },
    "Orders_bot": {
        "#order_monitor": "https://hooks.slack.com/services/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",
    }
}


def send_slack(block,slack_app_bot, slack_folder):
    payload = {
        "blocks": block,
    }
    try:
        response = requests.post(webhook[slack_app_bot][slack_folder], json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

"""
example call:
send_slack(block, "paymentv4","order_monitor")
"""









def demoapps(block):
    """Send a message to Slack using a webhook URL."""
    demoapp = "https://hooks.slack.com/services/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"

    payload = {
        "blocks": block,

    }

    try:
        response = requests.post(demoapp, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")


