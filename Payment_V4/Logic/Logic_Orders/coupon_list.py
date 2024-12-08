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



coupon_test = [
    "AlbumTest3",
]


coupon_albums = [
    "AlbumShip",
    "Album-Lior",
    "Album-isof",
    "AlbumFormat",
    "AlbumBundle",
    "AlbumTest6",
    "AlbumTest5",
    "AlbumTest4",
    "AlbumTest3",
    "AlbumTest2",
    "AlbumTest1",
    "AlbumTest"
]

coupon_calendar = [
    "AlbumShip",
    "Album-Lior",
    "Album-isof",
    "AlbumFormat",
    "AlbumBundle",
    "AlbumTest6",
    "AlbumTest5",
    "AlbumTest4",
    "AlbumTest3",
    "AlbumTest2",
    "AlbumTest1",
    "AlbumTest"
]



@pytest.mark.parametrize("coupon_code", coupon_albums)
def test_list(coupon_code):
    print(get_coupon(coupon_code))




# coupon_albums = coupon_albums + ["new_coupon"]