import time

import pytest
from playwright.sync_api import sync_playwright
from infra.generic_helpers import sql_updade_status_in_order_V3


class TestAddBookV3():
    @pytest.mark.smoke
    def test_api_request(self):
        with sync_playwright() as playwright:
            # Create a new API request context
            request_context = playwright.request.new_context()
            token = "be2b30408f834a74a66fbb863c4e589e"
            # Send a GET request
            response = request_context.get(f"https://payment-v4.lupa.co/api.aspx?method=add_basket&event_token={token}&eventtype=REGULAR&format=6&cover_type=0&page_type=5&theme=fish&pages=50&quantity=1&platform=app&source_type=books&source_device=mobile&flow=v4&lang=he&app_version=3.5.42.tf&device_type=ios&cloudcode=test&isCustomErr=false&token=FbQp8hnGcJy_k7JyihCpmPJtpzU2UHFeHT8QMQLsvTTKXe3Yph3DKeF710gy8Ultx4ZHAR44suPzBM0B_SdDJkioNGoE8BbM_0ek7-3ribMFYzf2zH8zddq-cwHgflGXNnITG4kno9vwM_y4kWeJE3RLWDb86DTR7F0TpLJyXjzwKtJdsUL_s1FJfHoPXLg-4Hy1NPkCHkNyTjhVjdrS40cebe1bypRUKVh8PHAkVl7epQPwrIo4bNwB9FLHAdLXXrTs5RcLPAPs6SXGMn88TvOqrq8Pw97NXzgoVOTX7RbHg06OcsQSmQHE11JcZSX-i9RDo6LQBN2blKZegZtnlg2")
            assert response.ok  # Verify response is successful (status 200-299)
            assert response.status == 200  # Verify HTTP status code

            # Parse JSON response
            # json_data = response.json()
            # assert json_data["id"] == 1  # Verify expected data in response
            time.sleep(5)
            sql_updade_status_in_order_V3()

            # Close the request context
            request_context.dispose()





