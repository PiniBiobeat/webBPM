from data_base import postgres_env






def coupon_value(coupon_code):
    getcoupon = f"SELECT x.* FROM cpn.coupon_tbl x WHERE name = '{coupon_code}' and use_date is null"
    setcoupon = postgres_env(getcoupon)
    print(setcoupon[1][2])


coupon_albums = {
    "AlbumShip": coupon_value,
    "Album-Lior": coupon_value,
    "Album-isof": coupon_value,
    "AlbumFormat": coupon_value,
    "AlbumBundle": coupon_value,
    "AlbumTest6": coupon_value,
    "AlbumTest5": coupon_value,
    "AlbumTest4": coupon_value,
    "AlbumTest3": coupon_value,
    "AlbumTest2": coupon_value,
    "AlbumTest1": coupon_value,
    "AlbumTest": coupon_value
}
#
coupon_albums1 = list(coupon_albums.keys())
coupon = coupon_value(coupon_albums1[0])

# for coupon_code in coupon_albums1:
#     coupon = coupon_value(coupon_code)
#     print(coupon)







# coupon_albums = {
#     "AlbumShip": coupon_value,
#     "Album-Lior": coupon_value,
#     "Album-isof": "Album-isof",
#     "AlbumFormat": "AlbumFormat",
#     "AlbumBundle": "AlbumBundle",
#     "AlbumTest6": "AlbumTest6",
#     "AlbumTest5": "AlbumTest5",
#     "AlbumTest4": "AlbumTest4",
#     "AlbumTest3": "AlbumTest3",
#     "AlbumTest2": "AlbumTest2",
#     "AlbumTest1": "AlbumTest1",
#     "AlbumTest": "AlbumTest"
# }


# coupon_calendar = {
#     "AlbumShip": "AlbumShip",
#     "Album-Lior": "Album-Lior",
#     "Album-isof": "Album-isof",
#     "AlbumFormat": "AlbumFormat",
#     "AlbumBundle": "AlbumBundle",
#     "AlbumTest6": "AlbumTest6",
#     "AlbumTest5": "AlbumTest5",
#     "AlbumTest4": "AlbumTest4",
#     "AlbumTest3": "AlbumTest3",
#     "AlbumTest2": "AlbumTest2",
#     "AlbumTest1": "AlbumTest1",
#     "AlbumTest": "SELECT x.* FROM cpn.coupon_tbl x WHERE name = 'AlbumTest' and use_date is null"
# }
#
#
#
# coupon_tiles = {
#     "AlbumShip": "AlbumShip",
#     "Album-Lior": "Album-Lior",
#     "Album-isof": "Album-isof",
#     "AlbumFormat": "AlbumFormat",
#     "AlbumBundle": "AlbumBundle",
#     "AlbumTest6": "AlbumTest6",
#     "AlbumTest5": "AlbumTest5",
#     "AlbumTest4": "AlbumTest4",
#     "AlbumTest3": "AlbumTest3",
#     "AlbumTest2": "AlbumTest2",
#     "AlbumTest1": "AlbumTest1",
#     "AlbumTest": "SELECT x.* FROM cpn.coupon_tbl x WHERE name = 'AlbumTest' and use_date is null"
# }