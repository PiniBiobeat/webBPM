import pytest
from playwright.sync_api import Page


class AddBookOnline:
    token = {
        "הגדה_פורמט_27_ריבועי_קטן": "https://paymentsv4-api.lupa.co.il/api.aspx?token=voayVzAotP4HNuITBlxU0ji-QvoOX6OU53X5j1816KTHLa5-bdvuTMa0sHA1vSAmiozuY8TYlIWTSdHSnoXVN_pUEgYHBK1ou5dhW3QuNRo6s_--ddULeGYg74LLCsEzfjdyF7BQ_EFm0nQeXk4XOJqjoH9BAYXSxJyg-9oaWoog092ay48oPgz-SEUfSCURbaUpl_OBJ7twA0z5BtWK7JIH2Wi2EHLLb9tLmOcRUQ9NCEwPAnHk6dJyFStcxivDFHxLoEk9RGKsBF0APxD3Ftmbe8ptqko_cm0QD8J58FZOCN1L7Sx8PSRj2udfrORRgefOnh2VvFeZjSdL3OdraQ2&event_token=05fab72be95d4e159503a270b9ee064b&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "הגדה_פורמט_35_ריבועי_גדול": "https://paymentsv4-api.lupa.co.il/api.aspx?token=voayVzAotP4HNuITBlxU0ji-QvoOX6OU53X5j1816KTHLa5-bdvuTMa0sHA1vSAmiozuY8TYlIWTSdHSnoXVN_pUEgYHBK1ou5dhW3QuNRo6s_--ddULeGYg74LLCsEzfjdyF7BQ_EFm0nQeXk4XOJqjoH9BAYXSxJyg-9oaWoog092ay48oPgz-SEUfSCURbaUpl_OBJ7twA0z5BtWK7JIH2Wi2EHLLb9tLmOcRUQ9NCEwPAnHk6dJyFStcxivDFHxLoEk9RGKsBF0APxD3Ftmbe8ptqko_cm0QD8J58FZOCN1L7Sx8PSRj2udfrORRgefOnh2VvFeZjSdL3OdraQ2&event_token=51d20130b6a04fb881e62e9a83c70af7&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "אלבום_לבדיקת_144_עמודים": "https://paymentsv4-api.lupa.co.il/api.aspx?token=PhxRNHuSfCpDXoeIz-4Ey4QctGmPNG2PSAexBEAgirHtYIHY-pFmwmszulGylYa2B_YzaUCETZ78Ap_B-AOIkvvp9hhelfuMTFc_5s4GYcKOiRWbXl33vd4DTOu5B5jlY9FgI8037klYhYSwfuo1GzQx3ArsjR72k3Q4VkGJE3eFlNtBlLqALLnJ9o2u4_O6G9jbs63qCELuLMK1UY1sMmJ8kIqfASAaD-Sh4QrUz6hjlnChv2KRm1pLngMwuOym_gVeGi5NJ8psU3VLH6MXMJ0FXeVnY2dLB-kVYtexIguW631pQeP6R2VeRbiySMeQDyjsjnXLgxPOepcbHtHN-w2&event_token=89f325c5d5d1411a8b959cd7fd21a8f5&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "פורמט_27_ריבועי_קטן_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=2a5d2c4ba3a146f1a88f53a0ca8e7869&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=mobile",
        "פורמט_27_ריבועי_קטן_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=4dcd4d4662f24c5aa6c50e9c71d785a0&device_type=web&lang=he&method=add_basket&format=27&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
        "פורמט_35_ריבועי_גדול_הולנדי": "https://paymentsv4-api.lupa.co.il/api.aspx?token=rT5kUOOPHFYs4r6uvhbmj6hsPUBN22lK7vrnvQoQVT0pqeXqtE4hQStRLxyFswqq4IMAVKYbh7-5YRbnYEF41-pI5VLhFzytOKOe71FsTUHbpuLStWwzyKU67jC4Qbvf_nd8pkWtqen3_GPXM-Ow0cAmnjHyMf9wItJeoUb5yx3JmF9PGNHPZqjPj5Q-dMrpm-_JCatXgc1mDWa2wvH8ugCrqkgCAvGIG4tRpyU5GLB-D-JjS6z2mn8CQfah3jwNiRW7L4KNJ5FDdWjdC_5qVLMqeY6K8j87YG2zedixmXKXkvRod-q38zUnMDqVH3pLhMunMUWL4mhncfJW3pgW6Q2&event_token=7a9c400e7e234808aab3ca45b5869232&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=5&quantity=1&source_type=books&source_device=mobile",
        "פורמט_35_ריבועי_גדול_קשה": "https://paymentsv4-api.lupa.co.il/api.aspx?token=xQKmTDzeZ3x_eGumi7NFtsYoGKUJFq18btE7XQIEmO8zlmtfzOu8lcg7lrdrRgT2X_RjaCULzrxM8lXMtm3pogQXpv5KL10mochlV4JetXNyrUFBKhAdGWBDvUrgp7LHLmusnojyzzyoSSou8nKjPfJDSF-UWhPqXWS63UekVl7aj7fsThOQ5NEL1aWLcZbRUgZuraMZnuygACp0IEowMHN7UxcvFARzbayt1ghHPmUjFOEd-GtJ9-uQBVcHewowGo1v4gQJtvYCxJhg3dYVFVogEjNwn1XSpr83nKWL4QWcvbq0FSnPz_osaYeM_w1EdVECHjj5Kmi1omn7I0_j3g2&event_token=9ec661a662bf4f4fbe883c6712e8d56b&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile",
    }


    def request_online(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.get(token)
        assert response.ok
        assert response.status == 200


class TestAddBookOnline:
    def test_api_request(self, page):
        AddBookOnline().request_online(page, "פורמט_27_ריבועי_קטן_רכה")