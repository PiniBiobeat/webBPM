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
        return print(f"more codes for {coupon_name}")


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

coupon = [
    "AlbumTest3",
]


@pytest.mark.parametrize("coupon_code", coupon)
def test_list(coupon_code):
    print(get_coupon(coupon_code))


coupon_calendar = {
    "AlbumShip": "AlbumShip",
    "Album-Lior": "Album-Lior",
    "Album-isof": "Album-isof",
    "AlbumFormat": "AlbumFormat",
    "AlbumBundle": "AlbumBundle",
    "AlbumTest6": "AlbumTest6",
    "AlbumTest5": "AlbumTest5",
    "AlbumTest4": "AlbumTest4",
    "AlbumTest3": "AlbumTest3",
    "AlbumTest2": "AlbumTest2",
    "AlbumTest1": "AlbumTest1",
    "AlbumTest": "SELECT x.* FROM cpn.coupon_tbl x WHERE name = 'AlbumTest' and use_date is null"
}

coupon_tiles = {
    "AlbumShip": "AlbumShip",
    "Album-Lior": "Album-Lior",
    "Album-isof": "Album-isof",
    "AlbumFormat": "AlbumFormat",
    "AlbumBundle": "AlbumBundle",
    "AlbumTest6": "AlbumTest6",
    "AlbumTest5": "AlbumTest5",
    "AlbumTest4": "AlbumTest4",
    "AlbumTest3": "AlbumTest3",
    "AlbumTest2": "AlbumTest2",
    "AlbumTest1": "AlbumTest1",
    "AlbumTest": "SELECT x.* FROM cpn.coupon_tbl x WHERE name = 'AlbumTest' and use_date is null"
}
