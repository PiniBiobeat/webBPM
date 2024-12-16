import pytest
from playwright.sync_api import Page


class AddCalendar:
    token = {
        "לוח_A3": "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=8df4a58283844dadaa4a85348fe027cd&source_type=calendars&source_device=mobile&token=H4J2o1-qsYwXcbxlgGsQQL05JR3sG91zuN_aW8GFqfKNmQcKSzn3_Pl3f8XzdrV1RyMwMpPDFRhLELB1cmOgQPQd7vUJoNQ37rQ20SwBf38de1OcpcJMwvyeSL_8x9KkaLw5AmPQ65R_4M2VxY4lgZJ1Jq0p8Wn4zWI5j2Kcry-Oj34Rf7gOf5AAp1xPnWlc2LgRsDD3w6lSoG-zVsMNtQ13yyML69LqT1byU4-lD97TtdS1vSZ__0RbER_sJBIGhA1LHGlyyV-lvaml9pz3NR3O7s95yKD3mFU7JXVlBIJEJYgMuQ5huNDPgCw-kVIWwY_yZPdhZdvbWOTtSNGsEw2",
        "לוח_A4": "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=533493647bc7472fb28ca3015d99f685&source_type=calendars&source_device=mobile&token=H4J2o1-qsYwXcbxlgGsQQL05JR3sG91zuN_aW8GFqfKNmQcKSzn3_Pl3f8XzdrV1RyMwMpPDFRhLELB1cmOgQPQd7vUJoNQ37rQ20SwBf38de1OcpcJMwvyeSL_8x9KkaLw5AmPQ65R_4M2VxY4lgZJ1Jq0p8Wn4zWI5j2Kcry-Oj34Rf7gOf5AAp1xPnWlc2LgRsDD3w6lSoG-zVsMNtQ13yyML69LqT1byU4-lD97TtdS1vSZ__0RbER_sJBIGhA1LHGlyyV-lvaml9pz3NR3O7s95yKD3mFU7JXVlBIJEJYgMuQ5huNDPgCw-kVIWwY_yZPdhZdvbWOTtSNGsEw2",
        "לוח_A5": "https://paymentsv4-api.lupa.co.il/api.aspx?method=add_basket&event_token=dde46b5fb1fd4a28b0ade670e73385cf&source_type=calendars&source_device=mobile&token=H4J2o1-qsYwXcbxlgGsQQL05JR3sG91zuN_aW8GFqfKNmQcKSzn3_Pl3f8XzdrV1RyMwMpPDFRhLELB1cmOgQPQd7vUJoNQ37rQ20SwBf38de1OcpcJMwvyeSL_8x9KkaLw5AmPQ65R_4M2VxY4lgZJ1Jq0p8Wn4zWI5j2Kcry-Oj34Rf7gOf5AAp1xPnWlc2LgRsDD3w6lSoG-zVsMNtQ13yyML69LqT1byU4-lD97TtdS1vSZ__0RbER_sJBIGhA1LHGlyyV-lvaml9pz3NR3O7s95yKD3mFU7JXVlBIJEJYgMuQ5huNDPgCw-kVIWwY_yZPdhZdvbWOTtSNGsEw2",

    }


    def request_calendar(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(token)
        assert response.ok
        assert response.status == 200


class TestAddCalendar:
    def test_api_request(self, page):
        AddCalendar().request_calendar(page, "לוח_A3")
        # AddCalendar().request_calendar(page, "לוח_A4")
        # AddCalendar().request_calendar(page, "לוח_A5")
