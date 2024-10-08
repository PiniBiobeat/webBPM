import requests

demoapp = "https://hooks.slack.com/services/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"

def send_slack_orders(block):
    """Send a message to Slack using a webhook URL."""
    paymentv4 = "https://hooks.slack.com/services/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"

    payload = {
        "blocks": block,

    }

    try:
        response = requests.post(paymentv4, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")