import time
import pytest
from playwright.sync_api import Page
from infra.generic_helpers import sql_updade_status_in_order_V3





class AddBookV3:

    token = {
        "אלבום לבדיקת 146 עמודים": "e36d5e7f64124e09b7a985933a6830f3",
        "פורמט 6 קלאסי פלוס הולנדי": "c185523cc38b4102a92950db007d8cfc",
        "פורמט 26 פנורמי הולנדי": "9f884ce291c54a429860d4ecb7fa57c9",
        "פורמט 27 ריבועי קטן הולנדי": "862bd344cae647c188ac1800f8b03848",
        "פורמט 35 ריבועי גדול הולנדי": "18715ed78d0341dea475363d0138694d",
        "פורמט 38 מיני לופה קשה / רכה": "16925c19e67d469aa3a2f1aef5c36bdb",
        "פורמט 6 קלאסי פלוס קשה": "84f4ba8a390b45f6927a3033894a9a60",
        "פורמט 26 פנורמי קשה": "70d9d57e2aee43a2869e5f83855d0dee",
        "פורמט 27 ריבועי קטן קשה /רכה": "a21fefee1d0845c0b50812b669183002",
        "פורמט 35 ריבועי גדול קשה": "be2b30408f834a74a66fbb863c4e589e"
    }

    def api_request(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(f"https://payment-v4.lupa.co/api.aspx?method=add_basket&event_token={token}&eventtype=REGULAR&format=6&cover_type=0&page_type=5&theme=fish&pages=50&quantity=1&platform=app&source_type=books&source_device=mobile&flow=v4&lang=he&app_version=3.5.42.tf&device_type=ios&cloudcode=test&isCustomErr=false&token=FbQp8hnGcJy_k7JyihCpmPJtpzU2UHFeHT8QMQLsvTTKXe3Yph3DKeF710gy8Ultx4ZHAR44suPzBM0B_SdDJkioNGoE8BbM_0ek7-3ribMFYzf2zH8zddq-cwHgflGXNnITG4kno9vwM_y4kWeJE3RLWDb86DTR7F0TpLJyXjzwKtJdsUL_s1FJfHoPXLg-4Hy1NPkCHkNyTjhVjdrS40cebe1bypRUKVh8PHAkVl7epQPwrIo4bNwB9FLHAdLXXrTs5RcLPAPs6SXGMn88TvOqrq8Pw97NXzgoVOTX7RbHg06OcsQSmQHE11JcZSX-i9RDo6LQBN2blKZegZtnlg2")
        assert response.ok
        assert response.status == 200
        time.sleep(5)
        sql_updade_status_in_order_V3()


class TestAddBookV3:
    def test_api_request(self, page):
        AddBookV3().api_request(page, "פורמט 35 ריבועי גדול קשה")