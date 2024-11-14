import time
import requests
from playwright.sync_api import sync_playwright

def test_check_api_request():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        api_request_found = False

        def log_request(request):
            nonlocal api_request_found
            if 'https://paymentsv4-api.lupa.co.il/api.aspx' in request.url:
                print(f"Captured desired API request: {request.url}")
                api_request_found = True

        # Set up the listener before navigation
        page.on('request', log_request)

        try:
            # Navigate to the page
            page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?&source_type=tiles&token=Mgxr0W4OG7n-JrsIluGGTKHJCx8Fsb4DbYn5fNYvFgmG9rc8glQaAHmxp-SJq1xNvJO2g0ahUDVSDWlelIInjRGEO9tEGL50phGnF-mkdKPful_buisslmuVJcdsGDN5WP76ciQDQp0O7WoHdHiFnOM6Q7T3cnF4yEcs07Rq1bfnUIExo4TdbtFkTieyzo9apnmU-UxrSU7bJM1WDb7AB_0ORM0I685yaVR8wBaakulP5LBUQtlZBYgqCDU_yp43SZ-72sJB_bjguroUM5mQ7s01fn4dW0EKhVrweRfYBsZE09FgPOUU7uiiFxz8whMVT6vNDM8VUMbkPC_lw0oyIg2&source_device=desktop&")

            # Wait for network idle or a specific element
            page.wait_for_load_state('networkidle', timeout=30000)

            if not api_request_found:
                print("API request not found. Checking page content...")
                # Additional checks or actions can be added here

            # Wait a bit longer to catch any delayed requests
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            send_slack(f"Error in API request check: {str(e)}")

        finally:
            if not api_request_found:
                send_slack("API request not found after checking all network requests.")
            else:
                print("API request was found successfully.")

            browser.close()

def send_slack(message):
    # Implement your Slack notification logic here
    print(f"Slack notification: {message}")

test_check_api_request()