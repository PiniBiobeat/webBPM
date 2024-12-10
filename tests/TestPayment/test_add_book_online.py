import pytest
from playwright.sync_api import Page


class AddBookOnline:
    token = {
        "פורמט_27_ריבועי_קטן_קשה_רכה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=4dcd4d4662f24c5aa6c50e9c71d785a0&device_type=web&lang=he&method=add_basket&format=27&cover_type=1&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "פורמט_27_ריבועי_קטן_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=2a5d2c4ba3a146f1a88f53a0ca8e7869&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=mobile",
        "פורמט_27_ריבועי_קטן_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=4dcd4d4662f24c5aa6c50e9c71d785a0&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "פורמט_35_ריבועי_גדול_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=7a9c400e7e234808aab3ca45b5869232&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=mobile",
        "פורמט_35_ריבועי_גדול_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=xQKmTDzeZ3x_eGumi7NFtsYoGKUJFq18btE7XQIEmO8zlmtfzOu8lcg7lrdrRgT2X_RjaCULzrxM8lXMtm3pogQXpv5KL10mochlV4JetXNyrUFBKhAdGWBDvUrgp7LHLmusnojyzzyoSSou8nKjPfJDSF-UWhPqXWS63UekVl7aj7fsThOQ5NEL1aWLcZbRUgZuraMZnuygACp0IEowMHN7UxcvFARzbayt1ghHPmUjFOEd-GtJ9-uQBVcHewowGo1v4gQJtvYCxJhg3dYVFVogEjNwn1XSpr83nKWL4QWcvbq0FSnPz_osaYeM_w1EdVECHjj5Kmi1omn7I0_j3g2&event_token=9ec661a662bf4f4fbe883c6712e8d56b&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",


    }


    def api_request_online(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(token)
        assert response.ok
        assert response.status == 200


class TestAddBookOnline:
    def test_api_request(self, page):
        AddBookOnline().api_request_online(page, "פורמט_35_ריבועי_גדול_הולנדי")

