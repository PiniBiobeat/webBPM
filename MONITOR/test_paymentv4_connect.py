import re
from playwright.sync_api import sync_playwright, expect
from slack import send_slack


class EmptyCartException(Exception):
    pass


def test_paymentv4_connect_book():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?source_device=mobile&source_type=books&token=pMyO3MaGpl92PHix28Lg-wbISxjkQS4S1Np8yCQagCpGPKzoX29zYyvi_ObIvjolrmKIjkZfbtiqXSoxNlyWY9qx0_dh-WH0Ozo62YddU57mM2Yy0lVAFigRTDatUSLUPMtvQKFI5EKbwrNPwerTyGBROIEwrI_tyGLVsZgmS25miom9_U-S2e3uCKnkbWOgSoMZfpPzhDbqszQCmN06WsD97NewrBwcgr0X7Xxs1ij24GKUb8sQRaUQgwxsQWOr-j9RmrGYDkzMyzoI0ZUdrhQuPgqtstDOqPzRAKcM0p9BhPlEQb0TIkTclwOVvIq6RRzKpyEbBIkV43LxOEG2qw2")
            try:
                expect(page.get_by_role("heading", name="זה לא אתם זה אנחנו")).to_be_visible()
                raise EmptyCartException()
            except AssertionError:
                pass
            expect(page.locator("#root")).to_contain_text("בואו נמשיך")
            expect(page.get_by_role("button", name="בואו נמשיך")).to_be_visible()
        except Exception as e:
            msg = type(e).__name__
            if msg == "AssertionError":
                put = "לא נמצאו אלמנטים"
            elif msg == "Error":
                put = "שגיאה בurl"
            elif msg == "EmptyCartException":
                put = "זה לא אתם זה אנחנו"
            else:
                put = str(e)


            block = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":alert: *תקלה: קופה למטה - ספרים וקלנדר* :alert:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Error Except:* {msg}: {put}"
                    }
                },
            ]
            send_slack(block,"paymentv4","#system_monitor")







def test_paymentv4_connect_tiles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?source_type=tiles&token=pMyO3MaGpl92PHix28Lg-wbISxjkQS4S1Np8yCQagCpGPKzoX29zYyvi_ObIvjolrmKIjkZfbtiqXSoxNlyWY9qx0_dh-WH0Ozo62YddU57mM2Yy0lVAFigRTDatUSLUPMtvQKFI5EKbwrNPwerTyGBROIEwrI_tyGLVsZgmS25miom9_U-S2e3uCKnkbWOgSoMZfpPzhDbqszQCmN06WsD97NewrBwcgr0X7Xxs1ij24GKUb8sQRaUQgwxsQWOr-j9RmrGYDkzMyzoI0ZUdrhQuPgqtstDOqPzRAKcM0p9BhPlEQb0TIkTclwOVvIq6RRzKpyEbBIkV43LxOEG2qw2")
            try:
                expect(page.get_by_role("heading", name="זה לא אתם זה אנחנו")).to_be_visible()
                raise EmptyCartException()
            except AssertionError:
                pass
            expect(page.locator("#root")).to_contain_text("בואו נמשיך")
            expect(page.get_by_role("button", name="בואו נמשיך")).to_be_visible()
        except Exception as e:
            msg = type(e).__name__
            if msg == "AssertionError":
                put = "לא נמצאו אלמנטים"
            elif msg == "Error":
                put = "שגיאה בurl"
            elif msg == "EmptyCartException":
                put = "זה לא אתם זה אנחנו"
            else:
                put = str(e)


            block = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":alert: *תקלה: קופה למטה - טיילס* :alert:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Error Except:* {msg}: {put}"
                    }
                },
            ]
            send_slack(block,"paymentv4","#system_monitor")



