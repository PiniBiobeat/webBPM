import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?source_device=mobile&source_type=books&token=fPon5DahDbeWopYCcxzXTnAGVt0aeH2JDwVIhEy5DeOu1HlPZr-OOMCkYIIBndkzP5Dyehgr8S6nzvsQ1NkaxqvhIX7wD4SV09trsj28fg8RO44luwaemoCav5F2T6NHZpJL1RqF5XckCOVlxMFBs0IP00a1sv0X840kgB2Xv5dVT0RPdkZ7YrUtubY5rSupBUUQ9X6hhgwJpzMxRrPmARybNbkpGld7uvx9tb8FsVIxk279kv0SCjKM0Q0UEUnj5wVEyEE9KMikQuK1vDUrFIeAnJSkaMWCcvdq02L8Tp4vkv9xhr9h-H4TQQ2R_pGuAL_PUc4l_e78t0QDQaACCQ2")
    page.goto("https://paymentsv4-ui.lupa.co.il/basketItems?source_device=mobile&source_type=books&token=fPon5DahDbeWopYCcxzXTnAGVt0aeH2JDwVIhEy5DeOu1HlPZr-OOMCkYIIBndkzP5Dyehgr8S6nzvsQ1NkaxqvhIX7wD4SV09trsj28fg8RO44luwaemoCav5F2T6NHZpJL1RqF5XckCOVlxMFBs0IP00a1sv0X840kgB2Xv5dVT0RPdkZ7YrUtubY5rSupBUUQ9X6hhgwJpzMxRrPmARybNbkpGld7uvx9tb8FsVIxk279kv0SCjKM0Q0UEUnj5wVEyEE9KMikQuK1vDUrFIeAnJSkaMWCcvdq02L8Tp4vkv9xhr9h-H4TQQ2R_pGuAL_PUc4l_e78t0QDQaACCQ2")
    page.get_by_role("button", name="בואו נמשיך").click()
    page.get_by_role("button", name="₪0.00").click()
    page.get_by_role("button", name="בואו נמשיך").click()
    page.get_by_label("עיר *").click()
    page.get_by_role("option", name="א ת עמק חפר").click()
    page.get_by_label("רחוב *").click()
    page.get_by_role("option", name="יוסי בנאי").click()
    page.get_by_label("רחוב *").fill("יוסי בנאי4")
    page.get_by_label("מספר בית *").click()
    page.get_by_label("מספר בית *").fill("3")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="לסיכום ההזמנה").click()
    page.get_by_role("checkbox", name="controlled").check()
    page.get_by_role("button", name="לתשלום").click()
    page.pause()

    # ---------------------
    context.close()
    browser.close()
