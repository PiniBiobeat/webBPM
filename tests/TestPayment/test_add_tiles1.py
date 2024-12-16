import os
from playwright.sync_api import sync_playwright
import pytest

url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&guid=d34f6cb66016403da613edc4e2a1d1f8&token=EdvXm_Wed54Yx-9sOj_bR_BSTF3NXYwvPOXr8qckQN90ubwBfndwyoB_S4-Os9UQLfsCfAiGvusB2qakh0eDuWxfSMuYHC36Q0ZfJ9xPns5_-yOzL-48K7Zvq6UbOw1O86-vGtsUDr-EaHJKhIzMftlEopcrquJ0kL_fGJipJiHO7K8W7O3PTG7yuelnx8grcSQAUZMgiYvOFsxAICCHQcZInm5p5lRYM3RuqgN_bpwXwrN25cKVszF4FnMbA5QMZShQxcjh7FfZ-VkuSz76qGxRzn6JBsKSHI8kF8-uaGmxNbTnBwoZw7n7-9yTHHT2sLbf-IEzUGJgrD-4j0blpg2&source_type=tiles&source_device=desktop"

@pytest.fixture
def headers():
    return {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://tiles.lupa.co.il/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'Cookie': os.getenv("COOKIE")
    }

@pytest.fixture
def payload():
    return "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":0,\"filter\":\"no\",\"frame_color\":\"black\",\"material\":\"frame\",\"tile_type\":\"photo\"}]"
@pytest.fixture
def payload_kapa():
    return "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":0,\"filter\":\"no\",\"frame_color\":\"noframe\",\"material\":\"kappa\",\"tile_type\":\"photo\"}]"


@pytest.fixture
def payload_frame_30():
    return "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":1,\"filter\":\"no\",\"frame_color\":\"noframe\",\"material\":\"kappa\",\"tile_type\":\"photo\"}]"




class TestAddTiles:

    #Frame 20*20
    def test_post_request_tiles_frame(self, page, headers, payload):

        response = page.context.request.post(
            url,
            headers=headers,
            data=payload
        )

        assert response.ok, f"POST request failed: {response.status}"
        assert response.status == 200
        response_json = response.json()
        assert response_json, "Response body is empty"
        print(response_json)

    # kapa 20*20
    def test_post_request_tiles_kapa(self, page, headers, payload_kapa):

        response = page.context.request.post(
            url,
            headers=headers,
            data=payload_kapa
        )

        assert response.ok, f"POST request failed: {response.status}"
        assert response.status == 200
        response_json = response.json()
        assert response_json, "Response body is empty"
        print(response_json)

    def test_post_request_tiles_frame_30(self, page, headers, payload_frame_30):

        response = page.context.request.post(
            url,
            headers=headers,
            data=payload_frame_30
        )

        assert response.ok, f"POST request failed: {response.status}"
        assert response.status == 200
        response_json = response.json()
        assert response_json, "Response body is empty"
        print(response_json)
