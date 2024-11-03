#page.py (page object model)
from playwright.sync_api import Page


class SearchPage:
    search_term_input_selector = '#sb_form_q'
    selector = "#finish"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("http://the-internet.herokuapp.com/dynamic_loading/1")

    def search(self):
        self.page.get_by_role("button", name="Start").click()
        self.page.get_by_role("heading", name="Hello World!").is_enabled()
        self.page.wait_for_selector(self.selector, state="visible")


#test_page.py desktop
def test_play(page):
    searchclass = SearchPage(page)
    searchclass.navigate()
    searchclass.search()


#test_page.py mobile
def test_play_mobile(page_mobile):
    searchclass = SearchPage(page_mobile)
    searchclass.navigate()
    searchclass.search()






































0
# #another example: Dependency Injection
# @pytest.fixture
# def searchclass(page: Page):
#     return SearchPage(page)
#
#
# def test_play2(searchclass):
#     searchclass.navigate()
#     searchclass.search()

0

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
