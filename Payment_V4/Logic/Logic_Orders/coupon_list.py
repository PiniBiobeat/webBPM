from data_base import postgres_env
import pytest


def get_coupon(coupon_name):
    try:
        getcoupon = f"SELECT * FROM cpn.coupon_tbl WHERE name = '{coupon_name}' and use_date is null and user_id = 0"
        setcoupon = postgres_env(getcoupon)
        if setcoupon[0][27] == "MANUAL_BY_CODE":
            return setcoupon[0][12]
        else:
            return coupon_name
    except:
        return coupon_name


def get_coupon_title(coupon_name):
    getcoupon1 = f"SELECT title FROM cpn.coupon_tbl WHERE name = '{coupon_name}'"
    coupon_title = postgres_env(getcoupon1)
    if coupon_title:
        return coupon_title[0][0]
    else:
        getcoupon2 = f"SELECT title FROM cpn.coupon_tbl WHERE code = '{coupon_name}'"
        coupon_title2 = postgres_env(getcoupon2)
        return coupon_title2[0][0]


# bundle sanity ------------------------------------------------

coupon_bundle = [
    "Test_Bundle_FIX",
    "Test_Bundle_₪_Quantity_Sal",
    "Test_Bundle_₪_sal_item",
    "Test_Bundle_₪_sal",
    "Test_Bundle_%_Item",
    "Test_Bundle_₪_Item",
    "Test_Bundle_Mix",
]

# album sanity ------------------------------------------------
# special

coupon_special_type = [
    "AlbumSpecialTypeCodeFix",
    "AlbumSpecialTypeNameFix",
    "AlbumSpecialTypeCodeSal_Item",
    "AlbumSpecialTypeNameSal_Item",
    "AlbumSpecialTypeCodeSal",
    "AlbumSpecialTypeCode%",
    "AlbumSpecialTypeCode",
    "AlbumSpecialTypeNameSal",
    "AlbumSpecialTypeName%",
    "AlbumSpecialTypeName",

]

coupon_haggadah = [
    None,
    "Test_Bundle_Haggadah",
    "AlbumHaggadahCodeShipPostSal%",
    "AlbumHaggadahNameShipPostSal",
    "AlbumHaggadahNameShipHome",
    "AlbumHaggadahCodeSal_Item",
    "AlbumHaggadahNameSal_Item",
    "AlbumHaggadahCodeSal",
    "AlbumHaggadahNameSal",
    "AlbumHaggadahCode%",
    "AlbumHaggadahName%",
    "AlbumHaggadahCode",
    "AlbumHaggadahName",
]

coupon_short_way = [
    None,
    "Test_Bundle_Mix",
    "AlbumShortWayCode",
    "AlbumShortWayName",
]

coupon_pay_for_40 = [
    "PayFor40_Code",
    "PayFor40_Name",
]

# ░░░░░░░░░░░░░░ ⬉ coupons special only for books ⬉ ░░░░░░░░░░░░░░

coupon_albums_type_code = [
    "AlbumTypeCodeSal_Double2",
    "AlbumTypeCodeSal_Double",
    "AlbumTypeCodeSal",
    "AlbumTypeCode%",
    "AlbumTypeCode",
]
coupon_albums_type_name = [
    "AlbumTypeNameSal",
    "AlbumTypeName%",
    "AlbumTypeName",
]

coupon_albums_fix = [
    "AlbumFixCodeShip",
    "AlbumFixNameShip",
    "AlbumFixCode",
    "AlbumFixName",
]

coupon_albums_shipping = [
    "AlbumShipCodeHomeSAL",
    "AlbumShipCodePostSAL",
    "AlbumShipCodeShopsSAL",
    "AlbumShipNameHomeSAL",
    "AlbumShipNamePostSAL",
    "AlbumShipNameShopsSAL",
    "AlbumShipCodeHome"
    "AlbumShipCodePost",
    "AlbumShipCodeShops",
    "AlbumShipNameHome",
    "AlbumShipNamePost",
    "AlbumShipNameShops",
]

coupon_albums_isof = [
    "Album-isof-Fix-Code",
    # "Album-isof-Fix-Name",
    "Album-isof-Code%",
    # "Album-isof-Name%",
    "Album-isof-Code"
    # "Album-isof-Name",
]

coupon_albums_items = [
    "AlbumTest6_per_Code",
    "AlbumTest5_per_Name",
    "AlbumTest4_items_Code",
    "AlbumTest3_items",
    "AlbumTest2_items_Code",
    "AlbumTest1_items"
]

coupon_albums = [
    "Album-All-Code",
    "AlbumTest12_campSal_Code",
    "AlbumTest10_campaign_Code",
    "AlbumTest9_campaign",
    "AlbumTest8_Code",
    "AlbumTest7",
    "AlbumTest6_Code",
    "AlbumTest5",
    "AlbumTest4_Code",
    "AlbumTest3",
    "AlbumTest2_Code",
    "AlbumTest1",
]

# Calendar sanity ------------------------------------------------

coupon_calendar_type_code = [
    "CalendarTypeCodeSal_Double2",
    "CalendarTypeCodeSal_Double",
    "CalendarTypeCodeSal",
    "CalendarTypeCode%",
    "CalendarTypeCode",
    "CalendarTypeCode",
]
coupon_calendar_type_name = [
    "CalendarTypeNameSal",
    "CalendarTypeName%",
    "CalendarTypeName",
]

coupon_calendar_fix = [
    "CalendarFixCodeShip",
    "CalendarFixNameShip",
    "CalendarFixCode",
    "CalendarFixName"
]

coupon_calendar_shipping = [
    "CalendarShipCodeHomeSAL",
    "CalendarShipCodePostSAL",
    "CalendarShipCodeShopsSAL",
    "CalendarShipNameHomeSAL",
    "CalendarShipNamePostSAL",
    "CalendarShipNameShopsSAL",
    "CalendarShipCodeHome",
    "CalendarShipCodePost",
    "CalendarShipCodeShops",
    "CalendarShipNameHome",
    "CalendarShipNamePost",
    "CalendarShipNameShops",
]

coupon_calendar_isof = [
    "Calendar-isof-Fix-Code",
    # "Calendar-isof-Fix-Name",
    "Calendar-isof-Code%",
    # "Calendar-isof-Name%",
    "Calendar-isof-Code"
    # "Calendar-isof-Name",
]

coupon_calendars_items = [
    "CalendarTest6_per_Code",
    "CalendarTest5_per_Name",
    "CalendarTest4_items_Code",
    "CalendarTest3_items",
    "CalendarTest2_items_Code",
    "CalendarTest1_items"
]

coupon_calendar = [
    "Calendar-All-Code",
    "Calendar-All-Name",
    "CalendarTest13_campaign%",
    "CalendarTest12_campSal_Code",
    "CalendarTest11_campSal",
    "CalendarTest10_campaign_Code",
    "CalendarTest9_campaign",
    "CalendarTest8_Code",
    "CalendarTest7",
    "CalendarTest6_Code",
    "CalendarTest5",
    "CalendarTest4_Code",
    "CalendarTest3",
    "CalendarTest2_Code",
    "CalendarTest1",
]

# Tiles sanity ------------------------------------------------

coupon_tiles_type_code = [
    "TilesTypeCodeSal_Double2",
    "TilesTypeCodeSal_Double1",
    "TilesTypeCodeSal",
    "TilesTypeCode%",
    "TilesTypeCode",
]
coupon_tiles_type_name = [
    "TilesTypeNameSal",
    "TilesTypeName%",
    "TilesTypeName",
]

coupon_tiles_fix = [
    "TilesFixCodeShip",
    "TilesFixNameShip",
    "TilesFixCode",
    "TilesFixName",
]

coupon_tiles_shipping = [
    "TilesShipCodeHomeSAL",
    "TilesShipCodePostSAL",
    "TilesShipCodeShopsSAL",
    "TilesShipNameHomeSAL",
    "TilesShipNamePostSAL",
    "TilesShipNameShopsSAL",
    "TilesShipCodeHome",
    "TilesShipCodePost",
    "TilesShipCodeShops",
    "TilesShipNameHome",
    "TilesShipNamePost",
    "TilesShipNameShops",
]

coupon_tiles_isof = [
    "Tiles-isof-Fix-Code",
    # "Tiles-isof-Fix-Name",
    "Tiles-isof-Code%",
    # "Tiles-isof-Name%",
    "Tiles-isof-Code",
    # "Tiles-isof-Name"
]

coupon_tiles_items = [
    "TilesTest6_per_Code",
    "TilesTest5_per_Name",
    "TilesTest4_items_Code",
    "TilesTest3_items",
    "TilesTest2_items_Code",
    "TilesTest1_items",
]

coupon_tiles = [
    "Tiles-All-Code",
    "Tiles-All-Name",
    "TilesTest13_campaign%",
    "TilesTest12_campSal_Code",
    "TilesTest11_campSal",
    "TilesTest10_campaign_Code",
    "TilesTest9_campaign",
    "TilesTest8_Code",
    "TilesTest7",
    "TilesTest6_Code",
    "TilesTest5",
    "TilesTest4_Code",
    "TilesTest3",
    "TilesTest2_Code",
    "TilesTest1",
]

# @pytest.mark.parametrize("coupon_code", coupon_albums)
# def test_list(coupon_code):
#     print(get_coupon(coupon_code))

# coupon_albums = coupon_albums + ["new_coupon"]
