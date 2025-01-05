from tests.TestTiles.test_add_to_payment import TilesToPayment
import json
import requests


class TilesToPayment1(TilesToPayment):

    def add_tiles_to_payment1(self):
        try:
            parent_test = TilesToPayment()
            parent_test.add_tiles_to_payment()

        except AssertionError as e:
            # Send a notification to Slack if the test fails
            self.send_slack_notification(f"Tiles not add to basket: {e}")
            raise  # Re-raise the exception to mark the test as failed

    def send_slack_notification(self, message_text):
        webhook_url = "https://hooks.slack.com/services/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"  # Replace with your actual Slack webhook URL

        # Create the message payload
        message = {
            "text": message_text,
            "channel": "#general"
        }

        # Convert the message payload to JSON format
        payload = json.dumps(message)

        try:
            # Send the message to Slack
            response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})

            # Check the response status code
            if response.status_code == 200:
                print("Message sent to Slack successfully.")
            else:
                print(
                    f"Failed to send the message to Slack. Status code: {response.status_code}, response: {response.text}")

        except requests.RequestException as error:
            print("Error sending message to Slack:", error)


# Instantiate and run the test
test_instance = TilesToPayment1()
test_instance.add_tiles_to_payment()
