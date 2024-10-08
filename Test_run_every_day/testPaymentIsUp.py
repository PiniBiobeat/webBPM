import asyncio
import requests
from playwright.async_api import async_playwright

# Slack webhook URL (replace with your actual webhook URL)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Function to send a message to Slack
def send_slack_message(message):
    payload = {"text": message}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raises an HTTPError if the request returned an unsuccessful status code
        print(f"Slack message sent: {message}")
    except Exception as e:
        print(f"Failed to send message to Slack: {e}")

async def check_element():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the webpage
        await page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?&source_type=tiles&token=m1ADjOA0J_mtuFN-wPgcZ7Akw0NzSS--4EtMcJK3g5ExejODBhvzDEcjOXxGUCyGVBHoW6ZGwyURy4ZEe9BgxxN5t5NYNYnkiZTlTWEMTo3FihfOb1wZSHzG3K1Pyl7eO_ToEDx1wbqYU2JtjagwsOPzNL2aexC4fhwX3C1Z_bi86fv-_SwMPQtBLchEPiDcgKTTIaerSxnvOblh58oNRsbyDImtItFj6Wbx9RDsNpK0cF9MQY_qk3sfx5rs25XNm9HMZDlFQRG7xn4nbpiApx4A6F0LQOBVkDt2ejg4rrHODMU_OlysBnvaQfNkzlFqH13V5Z4Ao8PKeDjsoDLbIg2&source_device=desktop&")

        # XPath for the element
        xpath_selector = '//*[@id="root"]/header/div'

        try:
            # Wait for the element and get its text content
            element = await page.wait_for_selector(f'xpath={xpath_selector}', timeout=5000)
            text_content = await element.text_content()

            # Print the extracted text content
            print(f"Element text: {text_content.strip()}")

        except Exception as e:
            # Send message to Slack if the element is not found
            error_message = f"Failed to find element at XPath: {xpath_selector}. Error: {str(e)}"
            send_slack_message(error_message)

        await browser.close()

# Run the function
asyncio.run(check_element())
