from playwright.sync_api import sync_playwright


def test_check_api_request():
    with sync_playwright() as p:
        # Start a browser and open a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Capture network requests
        def log_request(request):
            if 'https://paymentsv4-api.lupa.co.il/api.aspx' in request.url:
                print(f"Captured API request: {request.url}")

        # Add an event listener to capture all requests
        page.on('request', log_request)

        # Navigate to the page that triggers the API call
        page.goto("https://paymentsv4-ui.lupa.co.il/basket?source_type=tiles&token=LIKezgzQA5jXOcN7_piBvNtZ1et3xGx1O3Xp4DwyHImuKHnE37eN5fSv_mEZbidf5H_QhK_0MfmyZERsHqvEXo9BbRLkoHolS8uyCwBOHdlZiqfh5Gmgc05EQQzA9pXu1sIPc-N0Sd5XjDuMdBet-dj3cnxxvHad_uWvgMlmJXRjIJLntrKzYyPoNQAYYrGasVDbE2MO6ibBzT8xOJSgc8Tu967bECtNU3UV3illIFWZxJXo4EHq6je0f0qbWlUVDYQ5_45OTbYna5OdCtBR9FApjqtLPA8vFll2CzV7xeWRZX7AWdAm3Vl2YFQggR7PThgR37QWrWmqtYG5-zUeMw2&source_device=desktop")

        # Wait for the page to load or specific elements to appear
        page.wait_for_selector("text=בואו נמשיך", state="visible")

        # Close the browser
        browser.close()


test_check_api_request()
