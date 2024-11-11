import requests
from playwright.sync_api import sync_playwright

def check_api_request():
    with sync_playwright() as p:
        # Start a browser and open a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Flag to track if the desired API request is found
        api_request_found = False

        # Capture network requests
        def log_request(request):
            nonlocal api_request_found
            if 'https://paymentsv4-api.lupa.co.il/api.aspx' in request.url:
                print(f"Captured API request: {request.url}")
                api_request_found = True

        # Add an event listener to capture all requests
        page.on('request', log_request)

        # Navigate to the page that triggers the API call
        page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?&source_type=tiles&token=Mgxr0W4OG7n-JrsIluGGTKHJCx8Fsb4DbYn5fNYvFgmG9rc8glQaAHmxp-SJq1xNvJO2g0ahUDVSDWlelIInjRGEO9tEGL50phGnF-mkdKPful_buisslmuVJcdsGDN5WP76ciQDQp0O7WoHdHiFnOM6Q7T3cnF4yEcs07Rq1bfnUIExo4TdbtFkTieyzo9apnmU-UxrSU7bJM1WDb7AB_0ORM0I685yaVR8wBaakulP5LBUQtlZBYgqCDU_yp43SZ-72sJB_bjguroUM5mQ7s01fn4dW0EKhVrweRfYBsZE09FgPOUU7uiiFxz8whMVT6vNDM8VUMbkPC_lw0oyIg2&source_device=desktop&")

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

check_api_request()
