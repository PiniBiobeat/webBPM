import pytest
from playwright.sync_api import Page
from tests.TestPayment.get_token import get_token


class AddCalendar:
    token = get_token()
    print(token)
    items = {
        "לוח_A3": f"https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=8df4a58283844dadaa4a85348fe027cd&source_type=calendars&source_device=mobile&token={token}",
        "לוח_A4": f"https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=533493647bc7472fb28ca3015d99f685&source_type=calendars&source_device=mobile&token={token}",
        "לוח_A5": f"https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=dde46b5fb1fd4a28b0ade670e73385cf&source_type=calendars&source_device=mobile&token={token}",
    }


    def request_calendar(self, page, calendar_name):
        items = self.items.get(calendar_name)
        response = page.context.request.get(items)
        assert response.ok
        assert response.status == 200


class TestAddCalendar:
    def test_api_request(self, page):
        AddCalendar().request_calendar(page, "לוח_A3")
        AddCalendar().request_calendar(page, "לוח_A4")
        AddCalendar().request_calendar(page, "לוח_A5")
