


import re
from playwright.sync_api import sync_playwright, Page, expect

def test_example(page: Page) -> None:
    page.goto("https://tiles.lupa.co.il/")
    page.get_by_role("button", name="בחירת תמונות").click()
    page.locator(".rounded_box").first.click()
    page.locator("li").filter(has_text="ריבוע עם מסגרת20X20").click()
    page.get_by_label("").set_input_files("tests/TestTiles/shutterstock_711632317.jpg")
    page.goto("https://tiles.lupa.co.il/preview")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    test_example(page)
    page.wait_for_timeout(5000)
    browser.close()






# import os
# import pyautogui
# import time
#
#
#
# import subprocess
#
#
# def git_and_update_monitor():
#     server = "146.148.2.80"
#     username = "lupa"
#     password = "A12bc28!"
#     remote_path = r"C:\Users\lupa\Desktop\powergit.ps1"
#
#     ps_command = f"""
#     $username = '{username}'
#     $password = ConvertTo-SecureString '{password}' -AsPlainText -Force
#     $cred = New-Object System.Management.Automation.PSCredential($username, $password)
#
#     $session = New-PSSession -ComputerName {server} -Credential $cred
#     Invoke-Command -Session $session -ScriptBlock {{ Start-Process "{remote_path}" }}
#     Remove-PSSession $session
#     """
#
#     # הרצת הפקודה
#     process = subprocess.Popen(["powershell.exe", ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#
#     # הדפסת פלט אם יש
#     if stdout:
#         print(stdout.decode())
#     if stderr:
#         print(stderr.decode())
#
#
# git_and_update_monitor()
