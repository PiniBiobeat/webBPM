import time
import pytest
from playwright.sync_api import Page






class AddBookOnline:

    token = {"פורמט_35_ריבועי_גדול_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=8df4a58283844dadaa4a85348fe027cd&source_type=calendars&source_device=mobile&token=MezD497-BqMXp2leymF9iQF163sWy7zmHUdeMrgb20RR8jRAHl3GdpIVjbt6WdgNlDOZV-CA1m4Q7jaH_mHIFs7vZxV-GvRWm3yRfoUqzDFNIJKaJ8AbYcQhmANUX12Lxb4c00Zu_uBP1ul5UQ4YrEG2QKTmUuGiLnYbgIjQZDh4-Unw_yM50zpHtiQeZrVLqxqzgEViI1rVMAGtJlBv2UHxdBQMj8c8dsCrr0e4XcYi37pt30CDAQf96ZFl_QTMNahj57jct4A3a6X2FP9V9juukcBFDYbCdREJZ-7ICQjO6T5Ov7eg58t4W8T6ATFJCWowjom3cwYIOZ_1LFcV5A2"}



    def api_request(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(token)
        assert response.ok
        assert response.status == 200



class TestAddBookOnline:
    def test_api_request(self, page):
        AddBookOnline().api_request(page, "פורמט_35_ריבועי_גדול_קשה")