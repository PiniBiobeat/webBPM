from conftest import *




# page object modol desktop
class SearchPage():
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



def test_play(page):
    searchclass = SearchPage(page)
    searchclass.navigate()
    searchclass.search()




# page object modul mobile
class SearchPage2():
    search_term_input_selector = '#sb_form_q'
    selector = "#finish"

    def __init__(self, page_mobile: Page):
        self.page_mobile = page_mobile

    def navigate2(self):
        self.page_mobile.goto("http://the-internet.herokuapp.com/dynamic_loading/1")

    def search2(self):
        self.page_mobile.get_by_role("button", name="Start").click()
        self.page_mobile.get_by_role("heading", name="Hello World!").is_enabled()
        self.page_mobile.wait_for_selector(self.selector, state="visible")



def test_play2(page_mobile):
    searchclass2 = SearchPage2(page_mobile)
    searchclass2.navigate2()
    searchclass2.search2()

































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
