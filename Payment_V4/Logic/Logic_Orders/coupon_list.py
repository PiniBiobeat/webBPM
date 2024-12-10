from data_base import postgres_env
import pytest


def get_coupon(coupon_name):
    try:
        getcoupon = f"SELECT * FROM cpn.coupon_tbl WHERE name = '{coupon_name}' and use_date is null"
        setcoupon = postgres_env(getcoupon)
        if setcoupon[0][27] == "MANUAL_BY_CODE":
            return setcoupon[0][12]
        else:
            return coupon_name
    except:
        return coupon_name



#album sanity
coupon_albums_shipping = [
    "AlbumShipCodeHomeSAL",
    "AlbumShipCodePostSAL",
    "AlbumShipCodePointSAL",
    "AlbumShipNameHomeSAL",
    "AlbumShipNamePostSAL",
    "AlbumShipNamePointSAL",
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

coupon_albums_items = [
    "AlbumTest9_items_code"
    "AlbumTest8_items",
    "AlbumTest7_items",
]

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



#Calendar sanity
coupon_calendar_shipping = [
    "CalendarShipCodeHomeSAL",
    "CalendarShipCodePostSAL",
    "CalendarShipCodePointSAL",
    "CalendarShipNameHomeSAL",
    "CalendarShipNamePostSAL",
    "CalendarShipNamePointSAL",
    "CalendarShipCodeHome"
    "CalendarShipCodePost",
    "CalendarShipCodePoint",
    "CalendarShipNameHome",
    "CalendarShipNamePost",
    "CalendarShipNamePoint",
]

coupon_calendar_isof = [
    "Calendar-isof-Name",
    "Calendar-isof-Code"
]

coupon_calendars_items = [
    "CalendarTest9_items_code"
    "CalendarTest8_items",
    "CalendarTest7_items",
]

coupon_calendar = [
    "Calendar-All-Code",
    "Calendar-All-Name",
    "CalendarTest6",
    "CalendarTest5_Code",
    "CalendarTest4",
    "CalendarTest3_Code",
    "CalendarTest2",
    "CalendarTest1_Code",
    "CalendarTest"
]




#Tiles sanity
coupon_tiles_shipping = [
    "TilesShipCodeHomeSAL",
    "TilesShipCodePostSAL",
    "TilesShipCodePointSAL",
    "TilesShipNameHomeSAL",
    "TilesShipNamePostSAL",
    "TilesShipNamePointSAL",
    "TilesShipNameHome",
    "TilesShipNamePost",
    "TilesShipNamePoint",
    "TilesShipCodeHome"
    "TilesShipCodePost",
    "TilesShipCodePoint",
]

coupon_tiles_isof = [
    "Tiles-isof-Name",
    "Tiles-isof-Code"
]

coupon_tiles_items = [
    "TilesTest9_items_code"
    "TilesTest8_items",
    "TilesTest7_items",
]

coupon_tiles = [
    "Tiles-All-Code",
    "Tiles-All-Name",
    "TilesTest6",
    "TilesTest5_Code",
    "TilesTest4",
    "TilesTest3_Code",
    "TilesTest2",
    "TilesTest1_Code",
    "TilesTest"
]






@pytest.mark.parametrize("coupon_code", coupon_albums)
def test_list(coupon_code):
    print(get_coupon(coupon_code))




# coupon_albums = coupon_albums + ["new_coupon"]