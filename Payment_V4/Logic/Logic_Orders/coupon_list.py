from data_base import postgres_env
import pytest


def get_coupon(coupon_name):
    try:
        getcoupon = f"SELECT x.* FROM cpn.coupon_tbl x WHERE name = '{coupon_name}' and use_date is null"
        setcoupon = postgres_env(getcoupon)
        if setcoupon[0][27] == "MANUAL_BY_CODE":
            return setcoupon[0][12]
        else:
            return coupon_name
    except:
        return coupon_name




coupon_albums = [
    "Album-All-Code",
    "Album-All-Name",
    "AlbumTest6",
    "AlbumTest5_Code",
    "AlbumTest4",
    "AlbumTest3_Code",
    "AlbumTest2",
    "AlbumTest1_Code",
    "AlbumTest"
]

coupon_albums_items = [
    "AlbumTest4",
    "AlbumTest5",
    "AlbumTest6"
]


coupon_albums_shipping = [
    "AlbumShipNamePoint",
    "AlbumShipNamePost",
    "AlbumShipNameHome",
    "AlbumShipCodePoint",
    "AlbumShipCodePost",
    "AlbumShipCodeHome"

]

coupon_albums_isof = [
    "Album-isof-Name",
    "Album-isof-Code"
]
coupon_pay_for_40 = [
    "PayFor40_Code",
    "PayFor40_Name"
]



@pytest.mark.parametrize("coupon_code", coupon_albums)
def test_list(coupon_code):
    print(get_coupon(coupon_code))




# coupon_albums = coupon_albums + ["new_coupon"]