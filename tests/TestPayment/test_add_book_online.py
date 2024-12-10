import pytest
from playwright.sync_api import Page


class AddBookOnline:
    token = {
        "פורמט_27_ריבועי_קטן_קשה_רכה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=I31D902LOoD-pS9wDvE84hcf3LYPZqcjS3hbCil7DgUtm788NPld7rVEtLWvrIjWSA-5T4o3n10ZbeQQ4zOMsoyM-7vQIlh3EXi4vQHjtcHUh_7xh0T6I3jfnWZxHARngL7iD6ACiNflW83nvWyNr_8R2a4NMrOg161Re9QBfe4KT4x9NeQ1eETAKPmtW4Hs6E-VLvUuIgB1ypkaHvFnocIoc_WPsQgTSY9UFX62JntNxtf8_dXhSWXHEh7tPhOonc33xBF33q3uH12aCBTf_W38Xstpi0QN3rAultV5do8TkuyvQTWLyrDjJp0dGdWFGQCdiQnutWw8LyuRQsIfFQ2&event_token=9ec661a662bf4f4fbe883c6712e8d56b&device_type=web&lang=he&method=add_basket&format=27&cover_type=1&page_type=0&quantity=1&source_type=books&source_device=web",
        "פורמט_27_ריבועי_קטן_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=I31D902LOoD-pS9wDvE84hcf3LYPZqcjS3hbCil7DgUtm788NPld7rVEtLWvrIjWSA-5T4o3n10ZbeQQ4zOMsoyM-7vQIlh3EXi4vQHjtcHUh_7xh0T6I3jfnWZxHARngL7iD6ACiNflW83nvWyNr_8R2a4NMrOg161Re9QBfe4KT4x9NeQ1eETAKPmtW4Hs6E-VLvUuIgB1ypkaHvFnocIoc_WPsQgTSY9UFX62JntNxtf8_dXhSWXHEh7tPhOonc33xBF33q3uH12aCBTf_W38Xstpi0QN3rAultV5do8TkuyvQTWLyrDjJp0dGdWFGQCdiQnutWw8LyuRQsIfFQ2&event_token=9ec661a662bf4f4fbe883c6712e8d56b&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=web",
        "פורמט_27_ריבועי_קטן_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=I31D902LOoD-pS9wDvE84hcf3LYPZqcjS3hbCil7DgUtm788NPld7rVEtLWvrIjWSA-5T4o3n10ZbeQQ4zOMsoyM-7vQIlh3EXi4vQHjtcHUh_7xh0T6I3jfnWZxHARngL7iD6ACiNflW83nvWyNr_8R2a4NMrOg161Re9QBfe4KT4x9NeQ1eETAKPmtW4Hs6E-VLvUuIgB1ypkaHvFnocIoc_WPsQgTSY9UFX62JntNxtf8_dXhSWXHEh7tPhOonc33xBF33q3uH12aCBTf_W38Xstpi0QN3rAultV5do8TkuyvQTWLyrDjJp0dGdWFGQCdiQnutWw8LyuRQsIfFQ2&event_token=4dcd4d4662f24c5aa6c50e9c71d785a0&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=web",
        "פורמט_35_ריבועי_גדול_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=I31D902LOoD-pS9wDvE84hcf3LYPZqcjS3hbCil7DgUtm788NPld7rVEtLWvrIjWSA-5T4o3n10ZbeQQ4zOMsoyM-7vQIlh3EXi4vQHjtcHUh_7xh0T6I3jfnWZxHARngL7iD6ACiNflW83nvWyNr_8R2a4NMrOg161Re9QBfe4KT4x9NeQ1eETAKPmtW4Hs6E-VLvUuIgB1ypkaHvFnocIoc_WPsQgTSY9UFX62JntNxtf8_dXhSWXHEh7tPhOonc33xBF33q3uH12aCBTf_W38Xstpi0QN3rAultV5do8TkuyvQTWLyrDjJp0dGdWFGQCdiQnutWw8LyuRQsIfFQ2&event_token=7a9c400e7e234808aab3ca45b5869232&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=web",
        "פורמט_35_ריבועי_גדול_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=I31D902LOoD-pS9wDvE84hcf3LYPZqcjS3hbCil7DgUtm788NPld7rVEtLWvrIjWSA-5T4o3n10ZbeQQ4zOMsoyM-7vQIlh3EXi4vQHjtcHUh_7xh0T6I3jfnWZxHARngL7iD6ACiNflW83nvWyNr_8R2a4NMrOg161Re9QBfe4KT4x9NeQ1eETAKPmtW4Hs6E-VLvUuIgB1ypkaHvFnocIoc_WPsQgTSY9UFX62JntNxtf8_dXhSWXHEh7tPhOonc33xBF33q3uH12aCBTf_W38Xstpi0QN3rAultV5do8TkuyvQTWLyrDjJp0dGdWFGQCdiQnutWw8LyuRQsIfFQ2&event_token=9ec661a662bf4f4fbe883c6712e8d56b&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=web",

    }


    def api_request_online(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(token)
        assert response.ok
        assert response.status == 200


class TestAddBookOnline:
    def test_api_request(self, page):
        AddBookOnline().api_request_online(page, "פורמט_35_ריבועי_גדול_הולנדי")
