import requests



webhook_paymentv4 = {
    "demo_app": "https://hooks.slack.com/services/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",
    "order_monitor": "https://hooks.slack.com/services/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",
    "system_monitor": "https://hooks.slack.com/services/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",
}


def send_slack(block, user_paymentv4):
    """Send a message to Slack using a webhook URL."""
    payload = {
        "blocks": block,

    }
    try:
        response = requests.post(webhook_paymentv4[user_paymentv4], json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")













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


