import requests
from playwright.sync_api import sync_playwright

def test_check_api_request():
    with sync_playwright() as p:
        # Start a browser and open a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Flag to track if the desired API request is found
        api_request_found = False

        # Capture network requests
        def log_request(request):
            nonlocal api_request_found
            if 'https://paymentsv4-api.lupa.co/api.aspx' in request.url:
                print(f"Captured API request: {request.url}")
                api_request_found = True

        # Add an event listener to capture all requests
        page.on('request', log_request)

        # Navigate to the page that triggers the API call
        page.goto("https://paymentsv4-ui.lupa.co.il/basket?source_type=tiles&token=LIKezgzQA5jXOcN7_piBvNtZ1et3xGx1O3Xp4DwyHImuKHnE37eN5fSv_mEZbidf5H_QhK_0MfmyZERsHqvEXo9BbRLkoHolS8uyCwBOHdlZiqfh5Gmgc05EQQzA9pXu1sIPc-N0Sd5XjDuMdBet-dj3cnxxvHad_uWvgMlmJXRjIJLntrKzYyPoNQAYYrGasVDbE2MO6ibBzT8xOJSgc8Tu967bECtNU3UV3illIFWZxJXo4EHq6je0f0qbWlUVDYQ5_45OTbYna5OdCtBR9FApjqtLPA8vFll2CzV7xeWRZX7AWdAm3Vl2YFQggR7PThgR37QWrWmqtYG5-zUeMw2&source_device=desktop")

        # Wait for the page to load or specific elements to appear
        page.wait_for_selector("text=בואו נמשיך", state="visible")

        # After the page has loaded, check if the API request was found
        if not api_request_found:
            # Send a Slack notification if the request was not found
            send_slack("API request not found after checking all network requests.")

        # Close the browser
        browser.close()

def send_slack(message):
    slack_webhook_url = "https://hooks.slack.com/services/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"

    # Formatted message
    payload = {
        "text": message,  # Use the formatted message
        "username": "Order Monitor Bot",  # Bot name
        "channel": "#מוניטור-הזמנות",  # Slack channel
        "icon_emoji": ":camera:"  # Optional: Bot icon emoji
    }

    response = requests.post(slack_webhook_url, json=payload)

    # Handle Slack response
    if response.status_code != 200:
        print(f"Failed to send message to Slack. Status Code: {response.status_code}, Response: {response.text}")
    else:
        print("Message sent successfully to Slack!")

test_check_api_request()
