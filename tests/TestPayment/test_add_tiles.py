import os
from playwright.sync_api import Page
import pytest


class AddTiles:
    URL = "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&guid=d34f6cb66016403da613edc4e2a1d1f8&token=EdvXm_Wed54Yx-9sOj_bR_BSTF3NXYwvPOXr8qckQN90ubwBfndwyoB_S4-Os9UQLfsCfAiGvusB2qakh0eDuWxfSMuYHC36Q0ZfJ9xPns5_-yOzL-48K7Zvq6UbOw1O86-vGtsUDr-EaHJKhIzMftlEopcrquJ0kL_fGJipJiHO7K8W7O3PTG7yuelnx8grcSQAUZMgiYvOFsxAICCHQcZInm5p5lRYM3RuqgN_bpwXwrN25cKVszF4FnMbA5QMZShQxcjh7FfZ-VkuSz76qGxRzn6JBsKSHI8kF8-uaGmxNbTnBwoZw7n7-9yTHHT2sLbf-IEzUGJgrD-4j0blpg2&source_type=tiles&source_device=desktop"

    tiles_format = {
        "tiles20x20": "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":0,\"filter\":\"no\",\"frame_color\":\"black\",\"material\":\"frame\",\"tile_type\":\"photo\"}]",
        "tiles20x20white": "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":0,\"filter\":\"no\",\"frame_color\":\"white\",\"material\":\"frame\",\"tile_type\":\"photo\"}]",
        "tiles20X20kapa": "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":0,\"filter\":\"no\",\"frame_color\":\"noframe\",\"material\":\"kappa\",\"tile_type\":\"photo\"}]",
        "tiles30X30": "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":1,\"filter\":\"no\",\"frame_color\":\"black\",\"material\":\"frame\",\"tile_type\":\"photo\"}]",
        "tiles30X30kapa": "data=[{\"image_id\":\"d34f6cb66016403da613edc4e2a1d1f8.jpg\",\"border\":\"no\",\"format\":1,\"filter\":\"no\",\"frame_color\":\"noframe\",\"material\":\"kappa\",\"tile_type\":\"photo\"}]",
    }


    @staticmethod
    def _get_headers():
        return {
            'sec-ch-ua-platform': '"Windows"',
            'Referer': 'https://tiles.lupa.co.il/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'Cookie': os.getenv("COOKIE")
        }
    @classmethod
    def request_tiles(cls, page, tile_type):

        if tile_type not in cls.tiles_format:
            raise ValueError(f"Invalid tile type. Choose from: {list(cls.tiles_format.keys())}")
        payload = cls.tiles_format[tile_type]
        response = page.context.request.post(
            cls.URL,
            headers=cls._get_headers(),
            data=payload
        )
        assert response.ok, f"POST request failed: {response.status}"
        assert response.status == 200
        response_json = response.json()
        assert response_json, "Response body is empty"
        return response_json



class TestAddTiles:

    def test_tiles_request(self, page):
        AddTiles().request_tiles(page, "tiles20x20")
        AddTiles().request_tiles(page, "tiles20x20white")
        AddTiles().request_tiles(page, "tiles20X20kapa")
        AddTiles().request_tiles(page, "tiles30X30")
        AddTiles().request_tiles(page, "tiles30X30kapa")


