from playwright.sync_api import sync_playwright


def test_check_api_request():
    with sync_playwright() as p:
        # Start a browser and open a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(
            http_credentials={
                "username": "test",
                "password": "Acf325A12!"
            }
        )

        # Capture network requests
        def log_request(request):
            if 'https://payment-v4.lupa.co/api.aspx' in request.url:
                print(f"Captured API request: {request.url}")

        # Add an event listener to capture all requests
        page.on('request', log_request)

        # Navigate to the page that triggers the API call
        page.goto("https://paymentsv4-ui.lupa.co/basket?source_type=tiles&token=KrBj5sIGMqtV3N2izjSGZqsXfrVbhmiOV2RAej-9pEJB2NLuvZlhvssSDT46UobBjkPUgDDtyIvNELkSd5-3rnVGq0m-Rvhpp_qfzQf_Xp-HzANoLrvCc71EbRy3CrWktBvXM60Dpd0jtrW8gqJkXixwza-AtekytPdqBwwKTOp75Ii4XKugox7db2KTFAyKS7LvZJZzvJoLblb_4ws0-WTNdU8GlihrDoKQ8-qRZgOjVubp-miCfBhpgq34AfTFxnaJVxhhhmlLEtQoPhAMLQUdonDtu3HhohmgHTuNW3gXsMHfqbMy1VXHupgN5BfaKPTo9Jl-Ig75D5kMbFjgjw2&source_device=desktop")

        # Wait for the page to load or specific elements to appear
        page.wait_for_selector("text=בואו נמשיך", state="visible")

        # Close the browser
        browser.close()


test_check_api_request()